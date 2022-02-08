import logging
import os, sys
from unicodedata import decimal

from numpy import vdot
from scipy.fftpack import shift

sys.path.insert(0, ".")
from manim import *
from lib.scenes import *
from lib.objects import *
from lib.utils import *

ES_text_dict = {}

def create_bayes_theorem_header(scene):
    ES_text_dict["bayes_theorem_header"] = "bayes theorem definition"
    text_bayes = Text(ES_text_dict["bayes_theorem_header"], color=BLUE_E ).to_edge(UP)
    scene.play(Write(text_bayes))
    return text_bayes

def create_bayes_theorem_definition(scene,header):
    
    text_latex_bayes_def_left = Tex(r'$$P(A|B)$$').scale(1)
    text_latex_bayes_def_right = Tex(r'$$ = \frac{P(B|A)P(A)}{P(B)}$$').scale(1)

    pairs = [("left",text_latex_bayes_def_left) , ("right", text_latex_bayes_def_right)]
    group_latex_bayes_def = VDict(pairs,show_keys=False)

    text_latex_bayes_def_left.next_to(text_latex_bayes_def_right,direction=LEFT)
    group_latex_bayes_def.next_to(header,direction=DOWN)

    scene.play(Write(group_latex_bayes_def),run_time=14,lag_ratio=0.5)

    return group_latex_bayes_def

def create_bayesian_inference_header(scene, split_line):
    ES_text_dict["bayesian_inference_1"] = "1. belief uncertainty"
    ES_text_dict["bayesian_inference_2"] = "2. belief updates"

    text_keypoint_one = Text(ES_text_dict["bayesian_inference_1"],color=BLUE_E,font_size=24).to_edge(LEFT)
    text_keypoint_two = Text(ES_text_dict["bayesian_inference_2"],color=BLUE_E,font_size=24).to_edge(RIGHT)

    pairs = [("left_keypoint", text_keypoint_one) , ("right_keypoint", text_keypoint_two)]
    group_keypoints_inference = VDict(pairs,show_keys=False)

    text_keypoint_one.align_to(split_line,UP)
    text_keypoint_two.align_to(split_line,UP)

    scene.play(Write(group_keypoints_inference))
    return group_keypoints_inference

def create_inference_bulletpoint_one(scene, inference_bulletpoints_header):
    ES_text_dict["bayesian_inference_belief"] = "knowledge"
    ES_text_dict["bayesian_inference_uncertainty"] = "uncertainty"

    text_belief = Text(ES_text_dict["bayesian_inference_belief"],color=BLACK,font_size=20).to_edge(LEFT,buff=1.5)
    text_uncertainty = Text(ES_text_dict["bayesian_inference_uncertainty"],color=BLACK,font_size=20)

    text_belief.align_to(inference_bulletpoints_header["left_keypoint"],DOWN)
    text_belief.shift(DOWN*0.8)
    
    text_uncertainty.next_to(text_belief,RIGHT*4)

    double_arrow_belief_uncertainty = DoubleArrow(start=text_belief.get_right(),end=text_uncertainty.get_left(), color= BLUE_E)

    pairs = [("belief", text_belief) ,
             ("uncertainty", text_uncertainty),
             ("double_arrow" , double_arrow_belief_uncertainty) 
            ]

    header_keypoint_one = VDict(pairs, show_keys=False)

    scene.play(Write(text_belief))
    scene.play(Write(double_arrow_belief_uncertainty))
    scene.play(Write(text_uncertainty))

    return header_keypoint_one

def create_inference_bulletpoint_one_example(scene, inference_bulletpoint_one):

    text_latex_rain = Tex("$$P(rain) = $$").scale(1)
    text_latex_rain.to_corner(DL,buff=2)


    decimal = DecimalNumber(0.5, color=BLACK)
    decimal.next_to(text_latex_rain, direction=RIGHT)
    

    scene.play(Write(text_latex_rain))
    scene.wait(2)
    scene.play(FadeIn(decimal))
    scene.wait(8)
    scene.play(Indicate(inference_bulletpoint_one["uncertainty"],color=RED_E,run_time=4))
    scene.wait(22)
    scene.play(FadeOut(decimal))
    decimal.set_value(1.0)
    scene.play(FadeIn(decimal))
    scene.wait(1)
    scene.play(Indicate(inference_bulletpoint_one["belief"],color=RED_E,run_time=8))
    return text_latex_rain,decimal

def create_inference_bulletpoint_two(scene, inference_bulletpoints_header):

    text_belief = Text(ES_text_dict["bayesian_inference_belief"],color=BLACK,font_size=22).to_edge(RIGHT,buff=2.7)

    text_belief.align_to(inference_bulletpoints_header["right_keypoint"],DOWN)
    text_belief.shift(DOWN*0.8)   

    pairs = [("belief", text_belief)
            ]

    header_keypoint_two = VDict(pairs, show_keys=False)

    scene.play(Write(text_belief,run_time=2))
    scene.play(Circumscribe(text_belief,color=BLUE_B,time_width=3,fade_out=True))
    scene.play(Circumscribe(text_belief,color=BLUE_B,time_width=3,fade_out=True))
    scene.play(Circumscribe(text_belief,color=BLUE_B,time_width=3))



    return header_keypoint_two


def create_inference_bulletpoint_two_example(scene, inference_bulletpoints_header):
    ES_text_dict["list_bulletpoint_two"] = "- observations\n- events\n- information"
    
    txt = Text(ES_text_dict["list_bulletpoint_two"],color=BLACK,font_size=16).to_edge(RIGHT, buff= 5)
    txt.align_to(inference_bulletpoints_header["right_keypoint"],DOWN)
    txt.shift(DOWN*2)

    text_latex_rain = Tex("$$P(rain) = $$").scale(1).to_corner(DR,buff= 3)
    text_latex_rain.shift(DOWN*1)
    
    
    decimal_rain = DecimalNumber(0.5, color = BLACK)
    decimal_rain.next_to(text_latex_rain,direction=RIGHT)

    pairs = [ ("list_txt", txt), ("txt_latex", text_latex_rain), ("decimal", decimal_rain) ]

    bulletpoint_example_vdict = VDict(pairs,show_keys=False)

    scene.play(Write(txt,run_time=8.0))
    scene.wait(13)
    scene.play(Write(text_latex_rain))
    scene.play(Write(decimal_rain))
    scene.wait(26)
    scene.play(FadeOut(decimal_rain))
    decimal_rain.set_value(0.8)
    scene.play(FadeIn(decimal_rain))
    
    scene.wait(2)
    scene.play(Circumscribe(text_latex_rain,color=BLUE_B,time_width=3,fade_out=True))
    scene.play(Circumscribe(text_latex_rain,color=BLUE_B,time_width=3,fade_out=True))
    scene.play(Circumscribe(text_latex_rain,color=BLUE_B,time_width=3))
    scene.play(Indicate(txt), color=RED_E,run_time=14)
    scene.wait(1)

    return bulletpoint_example_vdict





class Main(Scene):
    def construct(self):

        video_name = r"bayes theorem intuition"
        play_intro_scene(self,video_name)
        timer = SceneTimer(self,debug_wait=False).reset()

        sfile = find_soundfile("01_bayes_theorem") 
        self.add_sound(sfile)
        
        self.next_section("1. Definition Bayes Theorem")
        timer.wait_until(3)
        bayes_theorem_intro = create_bayes_theorem_header(self)
        
        timer.wait_until(11)
        bayes_latex_theorem = create_bayes_theorem_definition(self, bayes_theorem_intro)
        timer.wait_until(35)

        self.play(Indicate(bayes_latex_theorem["left"]),color=RED_E,run_time=4)
        timer.wait_until(45)
        
        dot_bottom = Dot(color=BLUE_E)
        dot_bottom.to_edge(DOWN)

        split_line = Line(bayes_latex_theorem.get_bottom(), dot_bottom.get_center(),color=BLUE_E)
        self.play(Create(split_line))
        self.play(Create(dot_bottom))

        timer.wait_until("1min 2sec")
        self.play(bayes_latex_theorem.animate.scale(0.6))
        inference_bulletpoints_header = create_bayesian_inference_header(self,split_line)

        timer.wait_until("1min 15sec")
        self.play(Indicate(bayes_latex_theorem),color=RED_E,run_time=3)

        timer.wait_until("1min 33sec")
        self.play(Indicate(inference_bulletpoints_header["left_keypoint"]), color=RED_E,run_time=2)

        timer.wait_until("1min 36sec")
        inference_bulletpoint_one = create_inference_bulletpoint_one(self,inference_bulletpoints_header)      

        timer.wait_until("1min 55sec")
        inference_keypoint_one_example =  create_inference_bulletpoint_one_example(self,inference_bulletpoint_one)

        timer.wait_until("2min 45sec")
        self.play(Indicate(inference_bulletpoints_header["right_keypoint"]), color=RED_E,run_time=4)

        timer.wait_until("2min 51sec")
        inference_bulletpoint_two = create_inference_bulletpoint_two(self,inference_bulletpoints_header)

        timer.wait_until("2min 58sec")
        bulletpoint_two_example = create_inference_bulletpoint_two_example(self,inference_bulletpoints_header)


        self.play(*[FadeOut(mobject) for mobject in self.mobjects])

        timer.wait_until("4min 9sec")

        ### SECTION END ############

        self.next_section("2. Sun and Rain Example")
        
        sun_rain_example_title =  Text("sun and rain example", color=BLUE_E)
        self.play(FadeIn(sun_rain_example_title))
        timer.wait_until("4min 15sec")

        self.play(FadeOut(sun_rain_example_title,shift=DOWN))
        self.wait_until("4min 21sec")
        
        
        #timer.wait_until("17min 38sec")￼
        
