import numpy as np
import tensorflow as tf
import pandas as pd
from abc import ABC, abstractmethod
from typing import Optional, Dict
from pandas import DataFrame

class Sampler(ABC):

    @abstractmethod
    def set_seed(self, seed: Optional[int] = None):
        ...

    @abstractmethod
    def recover_seed(self):
        ...

    @abstractmethod
    def sample(
            self,
            n_samples: int
            ) -> DataFrame:
        ...

    def __call__(
            self,
            n_samples: int,
            seed: Optional[int] = None
            ) -> DataFrame:
        self.set_seed(seed)
        sample = self.sample(n_samples)
        self.recover_seed()
        return sample

class NumpySampler(Sampler):
    previous_state: Optional[Dict] = None

    def set_seed(self, seed: Optional[int] = None):
        if seed is not None:
            self.previous_state = np.random.get_state()
            np.random.seed(seed)

    def recover_seed(self):
        if self.previous_state is not None:
            np.random.set_state(self.previous_state)

class TensorflowSampler(Sampler):
    def set_seed(self, seed: Optional[int] = None):
        if seed is not None:
            tf.random.set_seed(seed)

    def recover_seed(self):
        return 

class FluSeasonContactSampler(NumpySampler):
    cond_dist = pd.DataFrame({
        "x_1": ["winter", "spring", "summer", "autumn"] * 2,
        "x_2": [0] * 4 + [1] * 4,
        "Pygx_1x_2": [0.6, 0.1, 0.05, 0.4, 0.7, 0.2, 0.1, 0.5]
        })

    def sample(
            self,
            n_samples: int,
            ) -> DataFrame:
        seasons = self.cond_dist.x_1.unique()
        samples = []
        for _ in range(n_samples):
            season = np.random.choice(seasons)
            x_2 = np.random.randint(2)
            prob = (
                    self
                    .cond_dist
                    .query("x_1 == @season & x_2 == @x_2")
                    .Pygx_1x_2
                    .values[0]
                    )
            y = np.random.binomial(1, prob)
            samples.append((season, x_2, y))
        samples_df = pd.DataFrame(samples, columns=["x_1", "x_2", "y"])
        return samples_df

class AnimalsFrequenciesSampler(NumpySampler):
    animals = ["dog", "cat", "bird", "fish"]
    weights = np.array([4, 4, 2, 1])
    def sample(
            self,
            n_samples: int,
            ) -> DataFrame:
        vals = np.random.uniform(0, 1, (n_samples, len(self.animals)))
        vals = vals * self.weights
        data = vals / vals.sum(axis=1, keepdims=True)
        samples_df = (
                pd.DataFrame(data, columns=self.animals)
                .assign(
                    house = np.arange(n_samples)
                    )
                )
        return samples_df

class LinearRegressionSampler(NumpySampler):
    def __init__(
            self,
            n_features: int=1, w_mean: float=1.0,
            w_std: float=1.0, noise_std: float=0.05
            ):
        self.n_features = n_features
        self.w_mean = w_mean
        self.w_std = w_std
        self.noise_std = noise_std

    def sample(self, n_samples: int) -> DataFrame:
        w = np.random.normal(
                self.w_mean,
                self.w_std,
                size=(self.n_features + 1, 1)
                )
        x = np.random.uniform(
                -10,
                10,
                size=(n_samples, self.n_features)
                )
        x_ones = np.hstack([np.ones((n_samples, 1)), x])
        noise = np.random.normal(
                0,
                self.noise_std,
                size=(n_samples, 1)
                )
        y = x_ones @ w + noise
        cols = ["x_" + str(i) for i in range(self.n_features)]
        data = (
                DataFrame(data=x, columns=cols)
                .assign(y=y)
                )
        return data
