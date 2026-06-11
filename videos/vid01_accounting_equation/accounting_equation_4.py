from manim import *

class ending(MovingCameraScene):
    def construct(self):
        # equation
        self.wait(2)
        t1 = Text("Assets = Liabilities + Equity",
                  font_size = 60,
                  font = "Patrick Hand SC")
        t1.move_to(ORIGIN)

        #surrounding rectangle 
        
        box = SurroundingRectangle(t1,
                                   color=YELLOW_C,
                                   stroke_width=4,
                                   buff=0.3   # space between text and box
                                   )
        
        self.add(box, t1)
        self.wait(1.5)
        # highlight
        # assets
        self.play(Indicate(t1[0:6],
                           scale_factor=1.05))
        self.wait(1.5)
        # liabilties
        self.play(Indicate(t1[7:18],
                           scale_factor=1.05))
        self.wait(1.5)
        # equity
        self.play(Indicate(t1[19:],
                           scale_factor=1.05))
        self.wait(1.5)

        # move equation slightly up
        equation = VGroup(t1, box)
        self.play(equation.animate.shift(UP * 0.5))

        # siapakah
        t2 = Text(" = Siapakah Pemilik kepada semua benda yang Business Miliki?",
                  font_size = 30,
                  font = "Patrick Hand SC")
        t2.next_to(equation, DOWN * 1)
        
        self.play(Create(t2[0:16]))
        self.wait(1.5)
        self.play(Create(t2[16:]))
        self.wait(2)


