
# Probabilistic Programming for Deep Learning

## running

we will use primarly `manim` community: https://github.com/ManimCommunity/manim/


build the docker image

      cd bin
       ./build-docker-image
      cd ..

make sure it is properly registered with your local docker installation (the image name is `manim`)

      docker image ls

render any video (runs in the container)

      ./bin/manim -ql src/probability/talking_about_probability/talking_about_probability.py 

notes:

- change `-ql` with `-qh` for rendering in high quality (takes longer)
- the folder `$HOME/Media` is mounted on the container as `/media` by the run script `bin/run`.
- place audio files under `$HOME/Media/audio` (thus, outside github)
- place images under `src/imgs` and include them in the github commits
- use `lib.objects.find_imgfile` and `lib.objects.find_audiofile` in your code to locate image or audio files on those folders.
- place there any files you might need for rendering 
- **output** will be rendered in `$HOME/Media/manim_output`


interactive session in the container:

    ./bin/run bash

## OBS configuration

      audio input capture built-it mic vol = -30
                          mic/aux vol = -20
                          filter noise supression RNNoise

      window capture composite
      video settings at 1920x1080, 60 FPS
      output encoder x264


## Intro music

seek for music which is royalty free, with no copyright.

https://www.youtube.com/watch?v=5_ps9cvmiTs&ab_channel=OblivionEpiphany

salsa intro from:

https://www.youtube.com/watch?v=0h7PMkiiqoA&ab_channel=LiborioConti


## manimgl

`manimgl` (the original package by 3b1b) contains examples, objects, etc. that could be useful.

- github repo: https://github.com/3b1b/manim
- github videos of the youtube channel: https://github.com/3b1b/videos
- a mirror github: https://gitcode.net/mirrors/3b1b/manim

Experiments using `manimgl` can be found under `refs/manimgl`. Use the `docker/Dockerfile` that you can find there to create a docker image with manimgl. Use `docker/run.sh` to render scenes. 

If you have an nvidia card, change the `FROM` line in `Dockerfile` and the `run.sh` script. 

include these lines in the main scene file to avoid over logging of debug from opengl

     import pyglet
     pyglet.options['debug_gl'] = False


## Audio Files known working configuration

If your video loses all audio or just a part try using the following `audio codec configuration` **tested on VLC media converter**

- Audio File Type: `wav`
- Codec: `MPEG Audio`
- Bitrate: `512 kb/s`
- Channels: `2`
- Sample Rate: `48000 Hz`

Since the original developers didnt intend for manim to be used with multiple large audio files, the internal audio libraries for `add_sound` do not implement audio parameters normalization.

As such, to ensure a proper video file generation, the audio files must be fixed prior to their incorporation in the video.

## FAQ and Common Issues

1. If video renders without audio, do the following:
      - Be sure to check the audio files configuration
      - Delete the specific video folder under `media/manim_output/videos/"YOUR_VIDEO_NAME"` to remove partial movie files that might be the cause of the issue
2. If video is missing frames/has weird jumps on animations:
      - Sometimes videos are rendered incorrectly, delete the video's folder and try again
      - Using two different timer objects can cause conflict, be sure to not use `SceneTimer Class` alongside `Scene` built-in timer ( For example, using `self.wait_until` and `timer.wait_until` )

