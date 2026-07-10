from manim import *
import numpy as np

CORAL = "#ed6f5c"
DARK = "#1a1a1a"


class SecanteTangente(Scene):
    def construct(self):
        self.camera.background_color = "#f7f1e6"

        def f(x):
            return 0.35 * x**2

        def fprime(x):
            return 0.7 * x

        axes = Axes(
            x_range=[-0.5, 5, 1],
            y_range=[-0.5, 8, 2],
            x_length=9,
            y_length=6,
            axis_config={"color": DARK, "stroke_width": 2},
            tips=False,
        )

        curve = axes.plot(f, x_range=[-0.3, 4.6], color=DARK, stroke_width=3)

        p_x = 1.6
        p_point = axes.coords_to_point(p_x, f(p_x))

        h_tracker = ValueTracker(2.6)

        def q_x():
            return p_x + h_tracker.get_value()

        def secant_line():
            qx = q_x()
            q_point = axes.coords_to_point(qx, f(qx))
            p_pt = axes.coords_to_point(p_x, f(p_x))
            direction = q_point - p_pt
            direction = direction / np.linalg.norm(direction)
            start = p_pt - direction * 5
            end = p_pt + direction * 5
            return Line(start, end, color=CORAL, stroke_width=4)

        def q_dot():
            qx = q_x()
            return Dot(axes.coords_to_point(qx, f(qx)), color=CORAL, radius=0.08)

        p_dot = Dot(p_point, color=DARK, radius=0.08)
        p_label = MathTex("P", color=DARK).next_to(p_dot, DOWN + LEFT, buff=0.15)

        secant = always_redraw(secant_line)
        q_d = always_redraw(q_dot)
        q_label = always_redraw(
            lambda: MathTex("Q", color=CORAL).next_to(q_dot(), UP + RIGHT, buff=0.15)
        )

        m_label = always_redraw(
            lambda: MathTex(
                rf"m_{{PQ}} = {fprime(p_x + h_tracker.get_value()/2):.2f}",
                color=DARK,
            )
            .scale(0.9)
            .to_corner(UR, buff=0.6)
        )

        self.play(Create(axes), Create(curve), run_time=1.2)
        self.play(FadeIn(p_dot), FadeIn(p_label), run_time=0.5)
        self.play(FadeIn(secant), FadeIn(q_d), FadeIn(q_label), FadeIn(m_label), run_time=0.6)
        self.wait(0.3)

        self.play(h_tracker.animate.set_value(0.02), run_time=4, rate_func=rate_functions.ease_in_out_sine)
        self.wait(0.3)

        tangent_slope = fprime(p_x)
        tangent = axes.plot(
            lambda x: f(p_x) + tangent_slope * (x - p_x),
            x_range=[-0.3, 4.6],
            color=CORAL,
            stroke_width=4,
        )
        final_label = MathTex(r"m = f'(P)", color=DARK).scale(0.9).to_corner(UR, buff=0.6)

        self.remove(secant, q_d, q_label, m_label)
        self.add(tangent, p_dot, p_label)
        self.play(FadeIn(final_label), run_time=0.6)
        self.wait(1.5)
