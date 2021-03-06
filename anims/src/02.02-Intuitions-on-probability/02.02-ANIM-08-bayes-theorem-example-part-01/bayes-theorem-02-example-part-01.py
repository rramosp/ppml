from gzip import WRITE
import logging
import os, sys
from unicodedata import decimal
from unittest import result

from numpy import vdot
from scipy.fftpack import shift

sys.path.insert(0, ".")
from manim import *
from lib.scenes import *
from lib.objects import *
from lib.utils import *

sys.path.insert(0, ".")

config.max_files_cached = 1000


class Main(Scene):
    def construct(self):
        
        video_name = r"bayes theorem example part 01"
        play_intro_scene(self, video_name)
        timer = SceneTimer(self, debug_wait=False).reset()

        sfile = find_soundfile("bayes-theorem-02-example-part-01-ES")
        self.add_sound(sfile)

        population_tex = MathTex(
            "POPULATION" , color= BLACK
        )

        timer.wait_until(22)
        
        self.play(Write(population_tex, run_time=2))

        timer.wait_until(27)

        with_medical_condition_circle = Circle(0.5, color = RED_E, fill_opacity = 0.6).shift(LEFT*1.2)
        without_medical_condition_circle = Circle(0.5,color= GREEN_E, fill_opacity = 0.6).next_to(with_medical_condition_circle,RIGHT,buff=1).shift(RIGHT*0.2)

        medical_condition_tex = MathTex(
            r"\text{medical condition}" , color= RED_E
        ).next_to(with_medical_condition_circle,DOWN).scale(0.6)

        no_medical_condition_tex = MathTex(
            r"\text{non medical condition}" , color= GREEN_E
        ).next_to(without_medical_condition_circle,DOWN).scale(0.6)

        with_medical_condition_vgroup = VGroup(with_medical_condition_circle,medical_condition_tex)
        without_medical_condition_vgroup = VGroup(without_medical_condition_circle, no_medical_condition_tex)
        
        wrapper_circles_with_label_vgroup = VGroup(with_medical_condition_vgroup,without_medical_condition_vgroup)

        self.play(population_tex.animate.shift(2*UP).scale(0.7))
        self.play(FadeIn(with_medical_condition_circle), FadeIn(without_medical_condition_circle))

        timer.wait_until(41)

        self.play(Write(medical_condition_tex), Write(no_medical_condition_tex))

        timer.wait_until(58)

        wrapper_population_with_definitions_vgroup = VGroup(wrapper_circles_with_label_vgroup, population_tex)
        wrapper_circles_with_label_vgroup.shift(UP*1.2)
        #surrounder_wrapper_popul_defs = SurroundingRectangle(wrapper_population_with_definitions_vgroup,color=BLACK,stroke_width=0.8)
        #complete_pop_def_vgroup = VGroup(wrapper_population_with_definitions_vgroup, surrounder_wrapper_popul_defs)
        complete_pop_def_vgroup = VGroup(wrapper_population_with_definitions_vgroup)
        
        self.play(complete_pop_def_vgroup.animate.to_edge(UP,buff=0.1).scale(0.9))

        p_disease = MathTex(
            "P(", "disease", ")", "=", "0.3", color=BLACK
        )
        p_disease.set_color_by_tex("disease",RED_E)

        timer.wait_until("1min 7sec")

        self.play(Write(p_disease,run_time=3))

        timer.wait_until("1min 24sec")

        p_positive_to_disease = MathTex(
            "P", "(" ,"positive", "|", "disease", ")", "=", "0.85", color= BLACK
        ).next_to(p_disease,DOWN)
        p_positive_to_disease.set_color_by_tex("disease",RED_E)

        self.play(FadeIn(p_positive_to_disease[0]), FadeIn(p_positive_to_disease[1]),
                FadeIn(p_positive_to_disease[3]),
                FadeIn(p_positive_to_disease[5])
        )

        timer.wait_until("1min 31sec")

        self.play(Write(p_positive_to_disease[4]))

        timer.wait_until("1min 36sec")

        self.play(Write(p_positive_to_disease[2]))
        
        timer.wait_until("1min 39sec")

        self.play(Write(p_positive_to_disease[-1]), Write(p_positive_to_disease[-2]))

        timer.wait_until("1min 57sec")

        self.play(Indicate(with_medical_condition_vgroup, color = RED_E,run_time=2))

        timer.wait_until("2min 0sec")

        updating_animation(p_positive_to_disease,self)

        timer.wait_until("2min 12sec")

        p_disease_to_positive = MathTex(
            "P", "(", "disease", "|", "positive",")", color= BLACK
        ).next_to(p_positive_to_disease,DOWN)

        p_disease_to_positive.set_color_by_tex("disease", RED_E)

        self.play(Write(p_disease_to_positive[0]), Write(p_disease_to_positive[1]),
                    Write(p_disease_to_positive[3]), Write(p_disease_to_positive[5]))


        timer.wait_until("2min 16sec")

        self.play(Write(p_disease_to_positive[4],run_time=2))
        self.play(Indicate(p_disease_to_positive[4],color=RED,run_time=4))


        timer.wait_until("2min 29sec")

        self.play(Write(p_disease_to_positive[2]))


        timer.wait_until("2min 42sec")

        equations_part_01 = VGroup(p_disease,p_disease_to_positive,p_positive_to_disease)

        self.play(equations_part_01.animate.to_corner(LEFT+UP,MED_SMALL_BUFF).shift(LEFT*0.5).scale(0.8))

        timer.wait_until("2min 45sec")

        bayes_p_disease_to_positive = MathTex(
            "P","(","disease","|","positive", ")" , "=", 
            "{P(","positive", "|", "disease", ")", "\cdot", "P(", "disease", ")",
            "\\over", "P(", "positive", ")}" , color= BLACK
        ).scale(0.7).shift(UP)
        bayes_p_disease_to_positive.set_color_by_tex("disease",RED_E)

        self.play(Write(VGroup(*bayes_p_disease_to_positive[0:7]),run_time=4))
        self.play(Write(VGroup(*bayes_p_disease_to_positive[7:]), run_time=6))

        timer.wait_until("3min 8sec")

        self.play(Indicate(VGroup(*bayes_p_disease_to_positive[0:6]),color=RED_E,run_time=2))

        timer.wait_until("3min 11sec")

        self.play(Indicate(VGroup(*bayes_p_disease_to_positive[7:12]),color=RED_E,run_time=2))
        updating_animation(p_positive_to_disease[-1], self)

        timer.wait_until("3min 16sec")

        self.play(Indicate(VGroup(*bayes_p_disease_to_positive[13:16]),color=RED_E,run_time=2))
        updating_animation(p_disease[-1],self)

        timer.wait_until("3min 22sec")

        self.play(Indicate(VGroup(*bayes_p_disease_to_positive[-3:]),color=RED_E,run_time=2))

        timer.wait_until("3min 28sec")

        p_positive = MathTex(
            "P(","positive", ")", "=", "P(", "positive", "|", "disease", ")","\cdot",
            "P(","disease",")", "+", "P(", "positive", "|", "\lnot disease", ")","\cdot", "P(", "\lnot disease", ")"
            , color=BLACK
        ).next_to(bayes_p_disease_to_positive,DOWN,buff=MED_LARGE_BUFF).scale(0.7)

        p_positive.set_color_by_tex("disease",RED_E)
        p_positive.set_color_by_tex("\lnot disease",GREEN_E)

        self.play(Write(VGroup(*p_positive[0:3])))

        timer.wait_until("3min 56sec")

        self.play(Write(p_positive[3]))

        timer.wait_until("3min 58sec")

        self.play(Write(p_positive[10:13],run_time=3))

        timer.wait_until("4min 7sec")

        self.play(Write(p_positive[4:10],run_time=3))

        timer.wait_until("4min 12sec")

        self.play(Write(p_positive[13]))

        timer.wait_until("4min 14sec")

        self.play(Write(p_positive[-3:]))

        timer.wait_until("4min 20sec")

        self.play(Write(VGroup(*p_positive[14:-3]), run_time=3))

        timer.wait_until("4min 25sec")

        self.play(Indicate(VGroup(*p_positive[0:3]),color=BLUE_E,scale_factor=1.1,run_time=3))

        timer.wait_until("4min 29sec")

        self.play(Indicate(VGroup(*p_positive[4:13]),color=RED_E,scale_factor=1.05,run_time=3))

        timer.wait_until("4min 33sec")

        self.play(Indicate(VGroup(*p_positive[14:]),color=GREEN_E,scale_factor=1.05,run_time=5))

        timer.wait_until("4min 44sec")

        p_disease_to_positive_long_equation = MathTex(
            "P(", "disease", "|", "positive", ")", "=" , "{P(", "positive", "|", "disease", ")", "\cdot", "P(", "disease", ")",
            "\\over",
            "P(", "positive", "|", "disease", ")","\cdot", # 16
            "P(", "disease", ")", "+", "P(", "positive", "|", "\lnot disease", ")","\cdot", "P(", "\lnot disease", ")}"
            , color=BLACK

        ).next_to(p_positive,DOWN,buff=MED_LARGE_BUFF).scale(0.8)

        p_disease_to_positive_long_equation.set_color_by_tex("disease",RED_E)
        p_disease_to_positive_long_equation.set_color_by_tex("\lnot disease",GREEN_E)

        self.play(FadeIn(p_disease_to_positive_long_equation))

        timer.wait_until("4min 46sec")

        p_positive_brace = Brace(VGroup(*p_disease_to_positive_long_equation[16:]), color=BLUE_E)

        self.play(Write(p_positive_brace))

        timer.wait_until("4min 48sec")

        trash_underline_p_positive_subtext = MathTex("P(positive)",color=BLACK).next_to(p_positive_brace,DOWN).scale(0.6)

        self.play(FadeIn(trash_underline_p_positive_subtext))

        timer.wait_until("4min 55sec")

        self.play(FadeOut(VGroup(p_positive_brace, trash_underline_p_positive_subtext)))
        
        timer.wait_until("4min 58sec")

        
        #upper_fraction_underline = Underline(VGroup(*p_disease_to_positive_long_equation[4:9], color= BLUE_E ))

        self.play(Indicate(VGroup(*p_disease_to_positive_long_equation[6:15]), color= BLUE_E),run_time=3)

        timer.wait_until("5min 1sec")

        lower_fraction_p_disease_underline = Underline(p_disease_to_positive_long_equation[22:25],color=RED_E)
        tex_p_disease_underline = MathTex(
            "0.3", color=BLACK
            ).scale(0.7).next_to(lower_fraction_p_disease_underline,DOWN)

        tex_p_disease_underline_copy = tex_p_disease_underline.copy().next_to(p_disease_to_positive_long_equation[12:15],UP,buff=SMALL_BUFF)

        self.play(Write(lower_fraction_p_disease_underline,run_time=3))

        timer.wait_until("5min 6sec")

        self.play(Write(tex_p_disease_underline), Write(tex_p_disease_underline_copy))

        timer.wait_until("5min 9sec")

        lower_fraction_p_not_disease_underline = Underline(p_disease_to_positive_long_equation[-3:],color=GREEN_E)
        tex_p_not_disease_underline = MathTex(
            "0.7", color=BLACK
            ).scale(0.7).next_to(lower_fraction_p_not_disease_underline,DOWN)

        self.play(Write(lower_fraction_p_not_disease_underline))
        self.play(Write(tex_p_not_disease_underline))

        timer.wait_until("5min 13sec")

        lower_fraction_p_positive_to_disease_underline = Underline(
            p_disease_to_positive_long_equation[16:21],
            color=RED_E)

        tex_p_pos_disease_underline = MathTex(
            "0.85",
             color=BLACK
        ).scale(0.7).next_to(lower_fraction_p_positive_to_disease_underline,DOWN)

        tex_p_pos_disease_underline_copy = tex_p_pos_disease_underline.copy().next_to(p_disease_to_positive_long_equation[6:11],UP,buff=SMALL_BUFF)

        self.play(Write(lower_fraction_p_positive_to_disease_underline), Write(tex_p_pos_disease_underline_copy))

        timer.wait_until("5min 18sec")

        self.play(Write(tex_p_pos_disease_underline))

        timer.wait_until("5min 23sec")

        self.play(Indicate(p_disease_to_positive_long_equation[16:21],color=RED_E),run_time=4)

        timer.wait_until("5min 29sec")

        updating_animation(VGroup(*p_disease_to_positive_long_equation[-9:-4]), self)
        updating_animation(VGroup(*p_disease_to_positive_long_equation[-9:-4]), self)
        updating_animation(VGroup(*p_disease_to_positive_long_equation[-9:-4]), self)
        updating_animation(VGroup(*p_disease_to_positive_long_equation[-9:-4]), self)
        updating_animation(VGroup(*p_disease_to_positive_long_equation[-9:-4]), self)

        timer.wait_until("6min 9sec")

        lower_fraction_p_pos_not_disease_underline = Underline(
            VGroup(*p_disease_to_positive_long_equation[-9:-4]), color = GREEN_E
        )

        tex_p_pos_not_disease_underline = MathTex(
            "0.05", color=BLACK
            ).scale(0.7).next_to(lower_fraction_p_pos_not_disease_underline,DOWN)

        self.play(Write(lower_fraction_p_pos_not_disease_underline))
        self.play(Write(tex_p_pos_not_disease_underline))

        timer.wait_until("6min 35sec")

        result_tex = MathTex(
            "P(disease|", "positive", ")" , "=", "{0.255",
             "\\over",
             "0.29}", "=", "0.879", color=BLACK
        ).next_to(p_disease_to_positive_long_equation,DOWN,buff=LARGE_BUFF)
        result_tex.set_color_by_tex("disease",RED_E)

        self.play(Write(result_tex[:4]),Write(result_tex[5]), run_time = 2)

        timer.wait_until("6min 38sec")
        
        self.play(ReplacementTransform(p_disease_to_positive_long_equation[4:9].copy(),
                                    result_tex[4]),
                 ReplacementTransform(p_disease_to_positive_long_equation[10:].copy(),
                                    result_tex[-3]) 
                )
        
        timer.wait_until("6min 42sec")

        self.play(Write(result_tex[-2:]))

        timer.wait_until("6min 48sec")

        updating_animation(VGroup(*p_disease_to_positive_long_equation[10:]),self)

        timer.wait_until("6min 59sec")

        self.play(Indicate(result_tex[0:3],color=BLUE_E,run_time=4))

        timer.wait_until("7min 21sec")

        self.play(Indicate(p_disease,color=RED_E,run_time=4))

        timer.wait_until("7min 27sec")

        self.play(Indicate(result_tex, color=RED_E),run_time=8)

        timer.wait_until("7min 46sec")

        updating_animation(result_tex[-1],self)

        timer.wait_until("7min 55sec")

        self.wait(5)
        play_credits(self)

        self.wait(5)

        
