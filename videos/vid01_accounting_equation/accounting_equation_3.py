from manim import *

class scene4(MovingCameraScene):
    def construct(self):
        # bus
        t1 = Text("Business",
                  font= "Patrick Hand SC",
                  weight=BOLD,
                  font_size=40,
                  color = WHITE)
        t1.move_to([0,0,0])
        self.play(Write(t1))
        self.wait(1.5)

        t2 = Text("Owner",
                  font= "Patrick Hand SC",
                  weight=BOLD,
                  font_size=40,
                  color = TEAL_A)
        t2.move_to([-3,0,0])
        self.play(Write(t2))
        self.wait(1.5)

        t3 = Text("Third Party",
                  font= "Patrick Hand SC",
                  weight=BOLD,
                  font_size=40,
                  color = ORANGE)
        t3.move_to([3,0,0])
        self.play(Write(t3))
        self.wait(1.5)

        # business takde apa apa
        box = RoundedRectangle( width=2.0,
                               height=3.0,
                               corner_radius=0.1)
        box.move_to([0,0,0])

        self.play(Create(box),
                  t1.animate.next_to(box, DOWN))
        self.wait(1.5)

        #tanda kosong
        arrow = CurvedArrow(start_point=[-2, 2.5, 0],
                            end_point=[-1.5, 1.2, 0],
                            angle=PI/3)   # controls curve)
        arrow.tip.scale(0.5)

        t4 = Text("takde apa",
                  font= "Patrick Hand",
                  weight=BOLD,
                  font_size=25)
        t4.move_to([-1.7,3,0])

        self.add(arrow, t4)
        self.wait(3)
        self.remove(t4)

        t5 = Text("alat (vehicle)",
                  font= "Patrick Hand",
                  weight=BOLD,
                  font_size=25)
        t5.move_to([-1.7,3,0])

        self.add(t5)
        self.wait(1.5)
        self.remove(arrow, t5)

        self.play(self.camera.frame.animate.shift(DOWN * 0.5),
                  run_time=1.5)
        self.wait(1.5)

        ### FILL

        # SMALL MARGIN so fills don't touch border
        margin = 0.07              # space between fill and border


        # LOWER FILL (60%)
        fill_bottom = Rectangle(width=2.0 - margin*2, # shrink width to avoid touching sides
                                height=(3.0 * 0.60) - margin, # slightly smaller height to avoid touching middle
                                fill_color=TEAL_A,
                                fill_opacity=1,
                                stroke_width=0)

        # position bottom fill inside box (with margin)
        fill_bottom.move_to(box.get_bottom()
                            + UP * (fill_bottom.height/2 + margin))


        # TOP FILL (25%)
        fill_top = Rectangle(width=2.0 - margin*2, # same width shrink
                             height=(3.0 * 0.40) - margin, # slightly smaller height
                             fill_color=ORANGE,
                             fill_opacity=1,
                             stroke_width=0)

        # position top fill inside box (with margin)
        fill_top.move_to(box.get_top() 
                         - UP * (fill_top.height/2 + margin))


        # ADD EVERYTHING (no animation, just display)
        self.play(TransformFromCopy(t2, fill_bottom))
        self.wait(1.5)
        self.play(TransformFromCopy(t3, fill_top))
        self.wait(1.5)

        # duplicate owner and liabilites

        self.play(Transform(fill_bottom, t2))
        self.wait(1.5)
        self.play(Transform(fill_top, t3))
        self.wait(1.5)

        # NOTE

