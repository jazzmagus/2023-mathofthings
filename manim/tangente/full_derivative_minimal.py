from manim import *

CORAL = "#ed6f5c"
DARK = "#1a1a1a"
BG = "#f7f1e6"
MUTED = "#8a8377"


class FullDerivativeMinimal(ThreeDScene):
    def construct(self):
        self.camera.background_color = BG

        # Scena 1: titolo
        title = Text("Cos'è una derivata?", font_size=56, color=DARK, weight=BOLD)
        subtitle = Text("Capire la pendenza di una curva", font_size=32, color=CORAL, slant=ITALIC)
        title.move_to(UP * 0.4)
        subtitle.next_to(title, DOWN, buff=0.35)

        self.play(FadeIn(title, shift=UP * 0.2), run_time=1)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=1)
        self.wait(1.2)
        self.play(FadeOut(title), FadeOut(subtitle), run_time=0.6)

        # Scena 2: dalla secante alla tangente

        axes = Axes(
            x_range=[-5, 5],
            y_range=[-2, 12, 2],
            x_length=7,
            y_length=5,
            axis_config={"include_tip": False, "color": DARK, "stroke_width": 2},
        ).shift(LEFT * 2)

        graph = axes.plot(lambda x: x ** 2, color=DARK, stroke_width=3, x_range=[-3.2, 3.2])
        graph_label = MathTex("f(x) = x^2", color=DARK, font_size=34).move_to(
            axes.c2p(-3.6, 10.5)
        )

        self.play(FadeIn(axes), run_time=0.6)
        self.play(Create(graph), Write(graph_label), run_time=1)
        self.wait(0.3)

        h = ValueTracker(3.0)
        x_val = -2

        dot_A = always_redraw(lambda: Dot(axes.c2p(x_val, x_val ** 2), color=DARK, radius=0.07))
        dot_B = always_redraw(lambda: Dot(axes.c2p(x_val + h.get_value(), (x_val + h.get_value()) ** 2), color=CORAL, radius=0.07))

        label_A = always_redraw(lambda: MathTex("A", font_size=30, color=DARK).next_to(dot_A, LEFT, buff=0.15))
        label_B = always_redraw(lambda: MathTex("B", font_size=30, color=CORAL).next_to(dot_B, UP, buff=0.15))

        secant_dynamic = always_redraw(lambda: Line(dot_A.get_center(), dot_B.get_center(), color=CORAL, stroke_width=3.5))

        caption = Text("La secante collega due punti sulla curva", font_size=26, color=MUTED).to_edge(DOWN, buff=0.4)

        self.play(FadeIn(dot_A, label_A, dot_B, label_B), run_time=0.6)
        self.play(Create(secant_dynamic, run_time=1.2), FadeIn(caption, run_time=0.6))
        self.wait(1.2)

        slope_formula = MathTex(r"\frac{f(x+h) - f(x)}{h}", color=DARK, font_size=38).to_edge(RIGHT).shift(DOWN * 0.75)

        caption2 = Text("È il tasso medio di variazione tra A e B", font_size=26, color=MUTED).to_edge(DOWN, buff=0.4)

        self.play(FadeTransform(caption, caption2), Write(slope_formula))
        self.wait(1.2)

        caption3 = Text("Quando B si avvicina ad A...", font_size=26, color=MUTED).to_edge(DOWN, buff=0.4)
        limit_eq = MathTex(r"\lim_{h \to 0} \frac{f(x+h) - f(x)}{h} = f'(x)", color=DARK, font_size=38).to_edge(RIGHT).shift(DOWN * 0.75)

        self.play(
            FadeTransform(caption2, caption3),
            FadeTransform(slope_formula, limit_eq),
            h.animate.set_value(0.15),
            run_time=3.5,
        )
        self.wait(1)

        caption4 = Text("...la secante diventa la tangente: la derivata", font_size=26, color=MUTED).to_edge(DOWN, buff=0.4)

        x_tracker = ValueTracker(-2)
        moving_dot = always_redraw(lambda: Dot(axes.c2p(x_tracker.get_value(), x_tracker.get_value() ** 2), color=DARK, radius=0.07))
        tangent_line = always_redraw(
            lambda: axes.plot(
                lambda x: x_tracker.get_value() ** 2 + 2 * x_tracker.get_value() * (x - x_tracker.get_value()),
                color=CORAL, stroke_width=3.5, x_range=[-3.2, 3.2],
            )
        )

        self.play(
            FadeTransform(caption3, caption4),
            h.animate.set_value(0.0),
            FadeIn(moving_dot),
            Create(tangent_line),
            FadeOut(dot_A), FadeOut(label_A), FadeOut(label_B), FadeOut(secant_dynamic), FadeOut(dot_B),
            run_time=1.5,
        )
        self.wait(0.8)

        tangent_label_static = MathTex(
            rf"f'({x_tracker.get_value():.0f}) = {2*x_tracker.get_value():.0f}", color=CORAL, font_size=32
        ).to_edge(RIGHT).shift(DOWN * 0.75)
        self.play(FadeTransform(limit_eq, tangent_label_static), run_time=0.8)
        self.remove(tangent_label_static)

        tangent_label = always_redraw(
            lambda: MathTex(rf"f'({x_tracker.get_value():.0f}) = {2*x_tracker.get_value():.0f}", color=CORAL, font_size=32)
            .to_edge(RIGHT).shift(DOWN * 0.75)
        )
        self.add(tangent_label)
        self.wait(0.6)

        for xv in [-1, 0, 1, 2]:
            self.play(x_tracker.animate.set_value(xv), run_time=1.1)
            self.wait(0.5)

        self.wait(0.8)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.6)
        self.wait(0.3)

        # Scena 3: piano tangente in 3D

        self.set_camera_orientation(phi=72 * DEGREES, theta=-70 * DEGREES)

        axes3d = ThreeDAxes(
            x_range=[-3, 3], y_range=[-3, 3], z_range=[0, 10],
            x_length=6, y_length=6, z_length=5,
            axis_config={"color": DARK, "stroke_width": 2},
        ).shift(IN * 2 + LEFT * 2)

        self.add(axes3d)

        caption3d = Text("La stessa idea, in tre dimensioni: il piano tangente", font_size=26, color=MUTED).to_edge(DOWN, buff=0.4)
        self.add_fixed_in_frame_mobjects(caption3d)
        self.play(FadeIn(caption3d), run_time=0.8)

        surface = Surface(
            lambda u, v: axes3d.c2p(u, v, u ** 2 + v ** 2),
            u_range=[-2.5, 2.5], v_range=[-2.5, 2.5],
            resolution=(28, 28),
            fill_opacity=0.55,
            checkerboard_colors=[DARK, "#2e2c28"],
            stroke_width=0.3,
            stroke_color=DARK,
        )

        a_tracker = ValueTracker(1)
        b_tracker = ValueTracker(1)

        moving_point = always_redraw(lambda: Dot3D(
            axes3d.c2p(a_tracker.get_value(), b_tracker.get_value(), a_tracker.get_value() ** 2 + b_tracker.get_value() ** 2),
            color=CORAL, radius=0.07,
        ))

        moving_plane = always_redraw(lambda: Surface(
            lambda u, v: axes3d.c2p(
                u, v,
                a_tracker.get_value() ** 2 + b_tracker.get_value() ** 2
                + 2 * a_tracker.get_value() * (u - a_tracker.get_value())
                + 2 * b_tracker.get_value() * (v - b_tracker.get_value())
            ),
            u_range=[a_tracker.get_value() - 1, a_tracker.get_value() + 1],
            v_range=[b_tracker.get_value() - 1, b_tracker.get_value() + 1],
            resolution=(8, 8),
            fill_opacity=0.75,
            checkerboard_colors=[CORAL, "#d65f4d"],
            stroke_width=0.3,
            stroke_color=CORAL,
        ))

        self.play(Create(surface), run_time=1.2)
        self.wait(0.4)
        self.play(FadeIn(moving_point), Create(moving_plane), run_time=1)
        self.wait(1)

        self.begin_ambient_camera_rotation(rate=PI / 3)
        self.wait(3)
        self.stop_ambient_camera_rotation()

        caption3d_2 = Text("Il piano segue il punto, ovunque si muova", font_size=26, color=MUTED).to_edge(DOWN, buff=0.4)
        self.add_fixed_in_frame_mobjects(caption3d_2)
        self.play(FadeTransform(caption3d, caption3d_2), run_time=0.6)

        self.play(a_tracker.animate.set_value(-1.2), b_tracker.animate.set_value(-1), run_time=1.8)
        self.play(a_tracker.animate.set_value(2.2), b_tracker.animate.set_value(1.5), run_time=1.8)
        self.play(a_tracker.animate.set_value(-1), b_tracker.animate.set_value(2), run_time=1.8)

        self.wait(0.8)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.6)
        self.wait(0.3)

        # Conclusione
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES)
        self.wait(0.3)

        summary = Text(
            "La derivata è la pendenza —\ndi una retta o di un piano — in un punto.",
            font_size=38, color=DARK, line_spacing=1.2,
        )
        self.play(FadeIn(summary, shift=UP * 0.2), run_time=1)
        self.wait(1.8)
        self.play(FadeOut(summary), run_time=0.8)
