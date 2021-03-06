from __future__ import division
from gzip import WRITE
import logging
import os, sys
from unicodedata import decimal

from numpy import vdot

sys.path.insert(0, ".")
from manim import *
from lib.scenes import *
from lib.objects import *
from lib.utils import *
import math

sys.path.insert(0, ".")


config.max_files_cached = 10000
Tex.set_default(color=BLACK)
Tex.set_default(stroke_color=BLACK)
Line.set_default(stroke_color=BLACK)
SingleStringMathTex.set_default(stroke_color=BLACK)
Text.set_default(color=BLACK,stroke_color=BLACK)

def pdf_curve_normal(x, mu, sigma):
            
    return math.exp(-((x-mu)**2)/(2*sigma**2))/(sigma*math.sqrt(2*math.pi))


class Main(Scene):
    def construct(self):

        video_name = r"bayes theorem continuous part 01"
        play_intro_scene(self, video_name)
        timer = SceneTimer(self, debug_wait=False).reset()

        sfile = find_soundfile("bayes-theorem-04-continuous-part-01-ES")
       
        self.add_sound(sfile)

        bayes_definition_tex = MathTex(
            "P", "(", "A", "|", "B", ")",
            "=",
            "{P(B|A)", "P(A)",
            "\\over",
            "P(B)} ", color=BLACK
        )

        p_z_to_s0 = MathTex(
            "P(", "z", "|", "s_{0}", "=", "22.3m", ")",
            "=",
            "{P(", "s_{0} = 22.3m", "|", "z", ") \cdot ", "P(z)",
            "\\over",
            "P(", "s_{0} = 22.3m", ")}", color= BLACK
        ).scale(0.8).to_edge(UP)

        
        timer.wait_until(1)

        self.play(
            Write(bayes_definition_tex)
        )

        timer.wait_until(8)

        self.play(
            Indicate(bayes_definition_tex[0:6], color=RED_E,scale_factor=1.08),
            Indicate(bayes_definition_tex[7], color=RED_E,scale_factor=1.08),
            Indicate(bayes_definition_tex[8], color=BLUE_E,scale_factor=1.08),
            Indicate(bayes_definition_tex[-1], color=BLUE_E,scale_factor=1.08),
            run_time=6
        )

        timer.wait_until(45)

        self.play(
            FadeOut(bayes_definition_tex)
        )
        

        ax = Axes(
            x_range = [-10, 10, 1],
            y_range = [0, 1, 0.2],
            axis_config = {    
                "stroke_color": BLACK,
                "include_tip": False    
            },
            x_axis_config={
                'numbers_to_include': [0],
                "include_ticks": False,
                "exclude_origin_tick": False
            },
            y_axis_config={
                'numbers_to_include': [0],
                "include_ticks": False
            }
        )

        tick_z = ax.get_axes()[0].get_tick(4).scale(2)

        zero_number_label = MathTex(
            "0", color=BLACK
        ).scale(0.8).move_to(
                        ax.get_axes()[0].get_number_mobject(0),
                    )


        z_number_label = MathTex(
            "Z", color=BLACK
        ).scale(0.8).move_to(
                        ax.get_axes()[0].get_number_mobject(4),
                    )


        sigma = ValueTracker(1)
        shifter_x_axis_pdf = ValueTracker(0)
    

        pdf_curve = always_redraw(
            lambda: ax.plot(
                lambda x: pdf_curve_normal(x + shifter_x_axis_pdf.get_value(), 0, sigma.get_value()), color=BLUE_E)
        )

        
        self.play(
            Write(ax.get_axes()[0]),
        )

        timer.wait_until(48)

        self.play(
            Write(z_number_label),
            Write(tick_z),
        )

        timer.wait_until(51)

        self.play(
            Indicate(z_number_label,color=RED_E),
            Indicate(tick_z,color=RED_E),
            run_time=4
        )

        timer.wait_until("1min")

        self.play(
            Write(zero_number_label)
        )

        timer.wait_until("1min 2sec")

        self.play(
            Indicate(zero_number_label,color=RED_E)
        )

        timer.wait_until("1min 5sec")

        origin_to_z_arrow = Arrow(
            start=zero_number_label.get_edge_center(RIGHT),
            end=z_number_label.get_edge_center(LEFT),
            color=BLUE_E
        )

        self.play(
            Write(origin_to_z_arrow)
        )

        timer.wait_until("1min 8sec")

        origin_to__negative_z_arrow = Arrow(
            start=zero_number_label.get_edge_center(RIGHT),
            end=z_number_label.get_edge_center(LEFT),
            color=RED_E
        ).next_to(zero_number_label,LEFT)

        origin_to__negative_z_arrow.rotate(PI)

        self.play(
            Write(origin_to__negative_z_arrow)
        )

        timer.wait_until("1min 20sec")

        self.play(
            Create(pdf_curve)
        )

        self.play(
            shifter_x_axis_pdf.animate.set_value(-1.5), run_time=1,
            rate_func=rate_functions.smooth
        )

        self.play(
            shifter_x_axis_pdf.animate.set_value(-2.5), run_time=1,
            rate_func=rate_functions.smooth
        )


        self.play(
            shifter_x_axis_pdf.animate.set_value(-4), run_time=1,
            rate_func=rate_functions.smooth
        )


        area_pdf_curve = always_redraw(lambda: ax.get_area(pdf_curve, color=RED_E, opacity=0.5))

        
        timer.wait_until("1min 31sec")

        self.play(
            sigma.animate.set_value(1.5), run_time=0.3,
            rate_func=rate_functions.smooth
        )

        self.play(
            sigma.animate.set_value(2), run_time=0.4,
            rate_func=rate_functions.smooth
        )

        self.play(
            sigma.animate.set_value(0.5), run_time=0.3,
            rate_func=rate_functions.smooth
        )
       

        self.play(
            sigma.animate.set_value(1), run_time=1,
            rate_func=rate_functions.smooth
        )

        timer.wait_until("1min 33sec")


 
        timer.wait_until("1min 36sec")


        

        timer.wait_until("1min 41sec")

        s_sub_i_tex = MathTex(
            "S_{i}",
            "\\rightarrow",
            "measurements \hspace{0.2cm} from \hspace{0.2cm} sensor", color=BLACK
        ).scale(0.8).to_edge(LEFT)

        self.play(
            Write(
                s_sub_i_tex[0]
            )
        )

        timer.wait_until("1min 44sec")

        self.play(
            Write(
                s_sub_i_tex[-1]
            )
        )

        self.play(
            Write(
                s_sub_i_tex[1]
            )
        )

        

        timer.wait_until("1min 49sec")

        s_sub_0_tex = MathTex(
            "S_{0}", "=", "22.3m", color=BLACK
        ).next_to(s_sub_i_tex,DOWN)
        
        self.play(
            Write(
                s_sub_0_tex[0]
            )
        )

        timer.wait_until("1min 55sec")

        self.play(
            Write(
                s_sub_0_tex[-1]
            )
        )


        self.play(
            Write(
                s_sub_0_tex[1]
            )
        )

        timer.wait_until("2min 1sec")
        
        s_sub_1_tex =  MathTex(
            "S_{1}", "=", "22.8m", color=BLACK
        ).next_to(s_sub_0_tex,DOWN)

        self.play(
            Write(
                s_sub_1_tex
            )
        )

        timer.wait_until("2min 10sec")

        z_tex = MathTex(
            "z"
        ).next_to(s_sub_1_tex,DOWN)

        self.play(
            Write(
                z_tex
            )
        )

        s_i_vgroup = VGroup(s_sub_i_tex,s_sub_0_tex, s_sub_1_tex, z_tex )

        timer.wait_until("2min 15sec")

        self.play(s_i_vgroup.animate.scale(0.8).to_corner(UL,buff=MED_SMALL_BUFF))

        timer.wait_until("2min 23sec")
        
        updating_animation(s_sub_0_tex,self)

        timer.wait_until("2min 36sec")

        self.play(
            Write(
                p_z_to_s0[0:7]
            )
        )

        updating_animation(p_z_to_s0[0:7],self)

        timer.wait_until("2min 42sec")

        updating_animation(p_z_to_s0[1],self, color=RED_E)

        timer.wait_until("2min 45sec")

        updating_animation(p_z_to_s0[3:7],self, color=GREEN_E)

        timer.wait_until("2min 58sec")

        self.play(
            FadeIn(
                p_z_to_s0[7:]
            )
        )

        updating_animation(p_z_to_s0[8:], self)

        timer.wait_until("3min 19sec")

        updating_animation(p_z_to_s0[13],self, color=GREEN_E)

        timer.wait_until("3min 23sec")

        prior_tex = MathTex(
            "Prior"
        ).scale(0.5).next_to(p_z_to_s0[13],UP)

        p_z_copy = p_z_to_s0[13].copy()

        self.play(
            Write(prior_tex)
        )

        self.play(
            p_z_copy.animate.next_to(s_sub_i_tex,RIGHT).scale(1).shift(RIGHT*7)
        )

        

        timer.wait_until("3min 34sec")

        p_s0_to_z = MathTex(
            "P(", "S_{0}", "|", "z", ")", color=BLACK
        ).scale(0.8).next_to(p_z_copy, DOWN)


        self.play(
            Write(
                p_s0_to_z[0:2]
            )
        )
        updating_animation(s_sub_0_tex,self,time_width=1.5)

        self.play(
            Write(
                p_s0_to_z[2:]
            )
        )

          
        timer.wait_until("3min 42sec")

        self.play(
            Indicate(
                p_s0_to_z[1], color=RED_E
            ),
            run_time=3
        )

        timer.wait_until("3min 46sec")

        self.play(
            Indicate(
                p_s0_to_z[3], color=GREEN_E
            ),
            run_time=2
        )

        timer.wait_until("3min 50sec")

        surrounder_p_s0_to_z = SurroundingRectangle(
            p_s0_to_z, color= BLUE_E
        )

        p_s0_to_z_likelihood_tex = MathTex(
            "Likelihood"
        ).scale(0.6).next_to(surrounder_p_s0_to_z, DOWN, buff=0.1)

        self.play(Create(surrounder_p_s0_to_z))
        self.play(Write(p_s0_to_z_likelihood_tex))

        timer.wait_until("3min 53sec")

        self.play(
            Uncreate(surrounder_p_s0_to_z),
            FadeOut(p_s0_to_z_likelihood_tex)
        )

        timer.wait_until("4min 5sec")

        std_1_m_tex = MathTex(
            "\\rightarrow", "std: ", "1","m"
        ).scale(0.8).next_to(p_s0_to_z,buff=SMALL_BUFF)


        self.play(
            Write(
                std_1_m_tex
            ),
            run_time=3
        )

        std_specification_graph_tex_left = MathTex(
            "1m"
        ).scale(0.6).next_to(z_number_label,UP).shift(LEFT*0.4).shift(UP)


        std_specification_graph_tex_right = MathTex(
            "1m"
        ).scale(0.6).next_to(z_number_label,UP).shift(RIGHT*0.4).shift(UP)

        t_label = ax.get_T_label(x_val=4, graph=pdf_curve, label=None, triangle_size=0, line_color=BLACK)

        self.play(
            Create(t_label)
        )

        horizontal_line_pdf = ax.get_horizontal_line(ax.input_to_graph_point(0.2,pdf_curve),color=BLACK)

        timer.wait_until("4min 9sec")


        self.play(
            Write(
                std_specification_graph_tex_left
            ),
            Write(
                std_specification_graph_tex_right
            )
        
        )

        self.play(Write(horizontal_line_pdf))

        timer.wait_until("4min 41sec")

        updating_animation(p_z_to_s0[13], self)

        timer.wait_until("4min 53sec")

        p_z_value = MathTex(
            "\\rightarrow" ,"prior"
        ).scale(0.8).next_to(p_z_copy,RIGHT)

        

        self.play(
            FadeIn(p_z_value)
        )

        timer.wait_until("4min 57sec")


        negative_hundred_number_label = MathTex(
        "-100", color=BLACK
        ).scale(0.8).move_to(
                    ax[0].get_number_mobject(-10),
                )
        
        hundred_number_label = MathTex(
        "100", color=BLACK
        ).scale(0.8).move_to(
                   ax[0].get_number_mobject(10),
                )        

        continuous_graph = always_redraw(lambda: ax.plot(lambda x: 0.4, x_range=[-10,10], color=GREEN_E))
        label_func_1 = ax.get_graph_label(graph=continuous_graph, label=MathTex("Continuous Function", color=GREEN_E).scale(0.8), x_val=-5,direction=UP )

        sigma.set_value(1)


        self.play(
            Create(ax),
            Write(label_func_1)
        )

        timer.wait_until("5min")

        self.play(
            Create(continuous_graph)
        )

        timer.wait_until("5min 3sec")

        self.play(
            Write(negative_hundred_number_label)
        )

        self.play(
            Write(hundred_number_label)
        )

        timer.wait_until("5min 30sec")

        self.play(FadeOut(z_number_label))

        z_number_label = MathTex(
            "20", color=BLACK
        ).scale(0.8).move_to(
                        ax.get_axes()[0].get_number_mobject(4),
                    )

        self.play(
            FadeIn(z_number_label)
            
        )

        timer.wait_until("5min 40sec")

        probabilities_vgroup = VGroup(p_z_copy,std_1_m_tex, p_z_value,p_s0_to_z)

        

        timer.wait_until("5min 41sec")

        label_func = ax.get_graph_label(graph=pdf_curve, label=MathTex("patata").scale(0.8), x_val=3,direction=UR )

        normal_tex = MathTex(
            "N(", "20", ",", "W", ")}", color=BLUE_E
        ).scale(0.8).move_to(label_func.get_center()).shift(RIGHT)

        self.play(
            Write(normal_tex[0:3])
        )
        
        timer.wait_until("5min 43sec")

        self.play(
            Write(normal_tex[3:])
        )

        timer.wait_until("5min 55sec")

        self.play(
            FadeOut(normal_tex[-2])
        )

        point_five_tex = MathTex(
            "0.5)", color=BLUE_E
        ).scale(0.8).move_to(normal_tex[-2]).shift(DOWN*0.02)

        timer.wait_until("6min")

        self.play(
            FadeOut(normal_tex[-1])
        )
        self.play(
            FadeIn(point_five_tex)
        )

        timer.wait_until("6min 25sec")

        self.play(
            Indicate(normal_tex[1], color=RED_E,scale_factor=1.15),
            run_time=3
        )

        timer.wait_until("6min 28sec")

        self.play(
            Indicate(point_five_tex, color=RED_E, scale_factor=1.15),
            run_time=3
        )

        timer.wait_until("6min 48sec")

        self.play(
            Uncreate(t_label),
            FadeOut(std_specification_graph_tex_left, std_specification_graph_tex_right)
        )

        

        timer.wait_until("6min 50sec")


        self.play(
            sigma.animate.set_value(2), run_time=3,
            rate_func=rate_functions.smooth
        )

        timer.wait_until("6min 55sec")

        t_label = ax.get_T_label(x_val=4, graph=pdf_curve, label=None, triangle_size=0, line_color=BLACK)

        self.play(
            Create(t_label)
        )

        timer.wait_until("7min 6sec")

        self.play(probabilities_vgroup.animate.scale(0.8).next_to(z_tex,DOWN))

        timer.wait_until("7min 8sec")

        
        timer.wait_until("7min 11sec")

        denominator_underline = Underline(p_z_to_s0[-3:], color=RED_E)

        self.play(
            Write(
                denominator_underline
            )
        )

        timer.wait_until("7min 13sec")

        normalization_factor_tex = MathTex(
            "normalization \hspace{0.2cm} factor"
        ).scale(0.5).next_to(denominator_underline,DOWN,buff=SMALL_BUFF)

        normalization_factor_evidence_tex = MathTex(
            "(evidence)"
        ).scale(0.5).next_to(normalization_factor_tex,DOWN,buff=0.01)

        self.play(
            Write(normalization_factor_tex),
            Write(normalization_factor_evidence_tex)
        )
    
        denominator_copy = p_z_to_s0[-3:].copy()

        self.play(denominator_copy.animate.next_to(p_s0_to_z,DOWN))

        timer.wait_until("7min 24sec")

        number_tex = MathTex(
            "\\rightarrow", "number"
        ).scale(0.8).scale(0.8).next_to(denominator_copy,RIGHT)

        self.play(
            Write(number_tex[-1])
        )

        self.play(
            Write(number_tex[0])
        )

        timer.wait_until("7min 36sec")

        updating_animation(p_z_copy,self,time_width=3)

        self.play(
            FadeOut(p_z_value[-1])
        )


        timer.wait_until("7min 40sec")

        prob_distribution_p_z_tex = MathTex(
            "N(", "20", "," ,"3", ")", "(z)"
        ).scale(0.8).scale(0.8).move_to(p_z_value[-1]).shift(RIGHT*0.35)

        self.play(
            Write(prob_distribution_p_z_tex[0])
        )

        timer.wait_until("7min 45sec")

        self.play(
            Write(prob_distribution_p_z_tex[1:5])
        )

        timer.wait_until("8min 6sec")

        self.play(
            Write(prob_distribution_p_z_tex[-1])
        )

        timer.wait_until("8min 10sec")

        updating_animation(p_s0_to_z, self)

        timer.wait_until("8min 15sec")

        buffer_arrow = MathTex(
            "\\rightarrow"
        ).scale(0.8).scale(0.8).next_to(p_s0_to_z, RIGHT)

        prob_distribution_p_s0_z_tex = MathTex(
            "N(", "z", "," ,"1", ")", "(22.3)"
        ).scale(0.8).scale(0.8).next_to(buffer_arrow,RIGHT,buff=0.1)

        self.play(
            FadeOut(
                std_1_m_tex
            )
        )

        self.play(
            Write(
                prob_distribution_p_s0_z_tex[0]
            ),
            Write(buffer_arrow)
        )

        timer.wait_until("8min 19sec")

        self.play(
            Write(
                prob_distribution_p_s0_z_tex[1]
            )
        )

        timer.wait_until("8min 29sec")

        self.play(
            Write(
                prob_distribution_p_s0_z_tex[2:5]
            )
        )

        timer.wait_until("8min 34sec")

        updating_animation(p_z_to_s0[9:11],self)

        self.play(
            Write(
                prob_distribution_p_s0_z_tex[-1]
            )
        )

        timer.wait_until("8min 40sec")

        self.play(
            Write(
                Underline(prob_distribution_p_s0_z_tex[:], color=RED_E)
            )
        )

        timer.wait_until("8min 42sec")

        updating_animation(prob_distribution_p_s0_z_tex[1], self)


        timer.wait_until("8min 45sec")

        updating_animation(prob_distribution_p_s0_z_tex[-1], self)

        timer.wait_until("8min 49sec")

        

        updating_animation(
            VGroup(p_z_copy,prob_distribution_p_z_tex),
            self
        )

        timer.wait_until("8min 52sec")

        self.play(
            Write(
                Underline(prob_distribution_p_z_tex,color=BLUE_E)
            )
        )

        timer.wait_until("8min 55sec")

        self.play(
            Indicate(
                prob_distribution_p_z_tex[1],
                color=RED_E
            )
        )

        timer.wait_until("9min 1sec")

        
        self.play(
            Indicate(
                prob_distribution_p_z_tex[-1],
                color=RED_E
            )
        )


        timer.wait_until("9min 5sec")

        self.play(
            Indicate(prob_distribution_p_z_tex,
            color=RED_E)
        )

        f_z_first = MathTex("\\rightarrow", "f(z)").scale(0.8).scale(0.8).next_to(prob_distribution_p_z_tex,RIGHT,buff=0.1)

        self.play(
            Write(
                f_z_first
            )
        )

        timer.wait_until("9min 10sec")

        self.play(
            Indicate(prob_distribution_p_s0_z_tex,
            color=BLUE_E)
        )

        f_z_second = MathTex("\\rightarrow", "f(z)").scale(0.8).scale(0.8).next_to(prob_distribution_p_s0_z_tex,RIGHT,buff=0.1)

        self.play(
            Write(
                f_z_second
            )
        )


        timer.wait_until("9min 19sec")

        self.play(
            Indicate(denominator_copy, color=GREEN_E),
            run_time = 3
        )


        timer.wait_until("9min 29sec")

        sum_denominator_tex = MathTex(
            "P(s_{0}=22.3m)", "=",
            "\int_{- \infty }^{ \infty }",
            "P(", "s_{0} = 22.3m", "|", "z)", "\cdot", "P(z)", " \,dz "
        ).scale(0.8).next_to(ORIGIN,UP).shift(RIGHT*3.3)

        self.play(
            FadeIn(
                sum_denominator_tex
            )
        )

        timer.wait_until("9min 37sec")

        self.play(
            Indicate(
                sum_denominator_tex[-7:], color=GREEN_E
            ),
            run_time=3
        )


        timer.wait_until("9min 40sec")

        updating_animation(p_z_to_s0[9:14],self, color=GREEN_E)

        timer.wait_until("10min 4sec")

        self.play(
            Indicate(sum_denominator_tex,color=GREEN_E),
            Indicate(number_tex[-1],color=GREEN_E),
            run_time=4
        )


        timer.wait_until("10min 14sec")

        self.play(
            Write(
                Underline(sum_denominator_tex[-7:-2], color=RED_E)
            )
        )
        
        timer.wait_until("10min 16sec")

        self.play(
            Write(
                Underline(sum_denominator_tex[-2:-1], color=BLUE_E)
            )
        )



        timer.wait_until("10min 26sec")

        updating_animation([prob_distribution_p_s0_z_tex, prob_distribution_p_z_tex], self, color=GREEN_E)


        timer.wait_until("10min 30sec")

        self.play(
            Indicate(sum_denominator_tex[-7:-3], color=GREEN_E, run_time=2)
        )

        self.play(
            Indicate(
                prob_distribution_p_s0_z_tex[1], color=GREEN_E
            ),
            run_time=3
        )

        timer.wait_until("10min 35sec")

        updating_animation(f_z_second[-1],self,color=GREEN_E)


        timer.wait_until("10min 38sec")

        self.play(
            Indicate(
                sum_denominator_tex[-2:-1],
                color=GREEN_E,
                run_time=2
            )
        )

        updating_animation(f_z_first[-1],self,color=GREEN_E)

        timer.wait_until("10min 42sec")

        integral_brace = Brace(sum_denominator_tex[-7:-1], buff=0.1, color=BLACK)

        self.play(
            FadeIn(
                integral_brace
            )
        )

        self.play(
            Write(
                MathTex("f(z)").scale(0.7).next_to(integral_brace,DOWN,buff=0.1)
            )
        )

        timer.wait_until("10min 51sec")

        ## STARTS MINI GRAPH

        ax2 = Axes(
            x_range=[0, 5],
            y_range=[0, 6],
            axis_config={"stroke_color": BLACK},
            x_axis_config={"numbers_to_include": [2, 3]},
            tips=False,
        )

        labels_2 = ax2.get_axis_labels().set_color(BLACK)

        curve_3 = ax2.plot(
            lambda x: 0.8 * x ** 2 - 3 * x + 4,
            x_range=[0, 4],
            color=GREEN_B,
        )

        line_1 = ax2.get_vertical_line(ax2.input_to_graph_point(2, curve_3), color=PURPLE_A)
        line_2 = ax2.get_vertical_line(ax2.i2gp(3, curve_3), color=PURPLE_A)

        
        area = ax2.get_area(curve_3, [2, 3], color=GREEN_E, opacity=0.4)

        any_function_vgroup = VGroup(
            ax2, labels_2, curve_3, line_1, line_2, area
        ).scale(0.3).shift(UP*0.8).shift(RIGHT*0.5).to_edge(UR,buff=SMALL_BUFF)

        surrounder_mini_graph = SurroundingRectangle(any_function_vgroup,color=RED_E)

        self.play(
            Write(
                ax2
            ),
            Write(
                labels_2
            ),
            Write(
                surrounder_mini_graph
            )
        )

        self.play(
            Create(
                curve_3
            )
        )

        timer.wait_until("10min 55sec")

        self.play(
            Write(line_1),
            Write(line_2)
        )

        timer.wait_until("10min 57sec")

        self.play(
            FadeIn(area)
        )


        ## ENDS MINI GRAPH


        
        ## credits
        self.wait(5)
        play_credits(self)

        self.wait(5)
        
