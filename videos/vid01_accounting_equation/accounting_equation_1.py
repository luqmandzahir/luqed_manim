from manim import *

class intro(Scene):
    def construct(self):
        t1 = Text("Accounting Equation",
                  font = "Patrick Hand SC",
                  font_size= 40
                  )
        t1.to_edge(UP)


        #persamaan accounting under
        t2 = Text("Persamaan Akaunting",
                  font = "Patrick Hand SC",
                  font_size = 25,
                  color = TEAL_B)
        t2.next_to(t1, DOWN, buff = 0.2)

        
        self.play(Write(t1))
        self.wait(1.5)
        self.play(Create(t2))
        self.wait(1.5)

        t3 = Text("Assets = Liabilities + Equity",
                  font_size = 60,
                  font = "Patrick Hand SC")
        t3.move_to(ORIGIN + UP*1.4)
        self.wait(1.5)
        
        self.add(t3[0:6])
        self.wait(1)
        self.add(t3[6])
        self.wait(1)
        self.add(t3[7:18])
        self.wait(1)
        self.add(t3[18])
        self.wait(1)
        self.add(t3[19:])         
        self.wait(1.5)

        #surrounding rectangle 
        
        box = SurroundingRectangle(t3,
                                   color=YELLOW_C,
                                   stroke_width=4,
                                   buff=0.3   # space between text and box
                                   )
        
        self.play(Create(box), run_time = 1)
        self.wait(1.5)

        #create dot in the middle
        d = Dot(radius = 0.07, color = TEAL_D)
        self.play(Write(d))
        self.wait(1.5)

        #focus
        t4 = Text("Focus Kita:",
                  font_size = 30,
                  font = "Patrick Hand SC",
                  weight = BOLD,
                  color = BLUE_B)
        
        self.play(d.animate.next_to(t4, LEFT, buff = 0.2))
        self.wait(1.5)
        self.play(Write(t4))
        self.wait(1.5)

        #logic
        t5 = Text("Apakah Logic Disebalik Persamaan Ni?",
                  font_size = 32,
                  font = "Patrick Hand SC",
                  color = BLUE_B)
        t5.next_to(t4, DOWN, buff = 0.3)
        
        self.play (Create(t5))
        self.wait(2)
        
        dt4t5 = VGroup(d, t4, t5)
        t3box = VGroup(t1,t2,t3,box)
        self.play(FadeOut(dt4t5),t3box.animate.move_to(ORIGIN + UP*1), run_time = 2)
        self.wait(1.5)

        t6 = Text("Idea yang membina dunia perakaunan!",
                  font_size = 32,
                  font = "Patrick Hand SC",
                  color = BLUE_B)
        t6.next_to(t3, DOWN, buff = 0.6)

        self.play (Create(t6))
        self.wait(2)

        # remain t1 and t2 on top and fade others
        t1t2 = VGroup(t1, t2)
        others = VGroup(t3, box, t6)
        
        self.play(FadeOut(others), t1t2.animate.move_to([0,1.5,0]), run_time = 2)
        self.wait(2)


class scene1(Scene):
    def construct(self):
        t1 = Text("Accounting Equation",
                  font = "Patrick Hand SC",
                  font_size= 40
                  )
        t1.move_to([0,1,0])


        #persamaan accounting under
        t2 = Text("Persamaan Akaunting",
                  font = "Patrick Hand SC",
                  font_size = 25,
                  color = TEAL_B)
        t2.next_to(t1, DOWN)

        
        self.add(t1,t2)
        self.wait(1.5)

        #create a box surrounding
        t1t2 = VGroup(t1, t2)

        box = SurroundingRectangle(t1t2,
                                   color=YELLOW_C,
                                   stroke_width=4,
                                   buff=0.3   # space between text and box
                                   )
        
        self.play(Create(box), run_time = 1)
        self.wait(1.5)

        t3 = Text("Logic: Semua benda yang business ada, mesti akan ada orang yang claim.",
                  font = "Poppins",
                  font_size = 23)
        t3.next_to(t2, DOWN, buff = 0.9)

        self.play(Create(t3[0:6]))
        self.wait(1.5)
        self.play(Create(t3[6:32]), run_time = 2)
        self.wait(1.5)
        self.play(Create(t3[32:]), run_time = 2)
        self.wait(1.5)

        #underline
        un1 = Underline(t3[20:32],
                        color = TEAL_A)
        self.play(Write(un1))
        self.wait(1.5)

        un2 = Underline(t3[44:],
                        color = TEAL_A)
        self.play(Write(un2))
        self.wait(2)

class scene2(Scene):
    def construct(self):
        t1 = Text("Tapi? Kenapa Pulak?",
                  font = "Poppins",
                  font_size = 28)
        t1.move_to([0,1.5,0])

        self.add(t1[0:5])
        self.wait(1.5)
        self.add(t1[5:])
        self.wait(1.5)
        self.play(Uncreate(t1))
        self.wait(2)

class scene3(Scene):
   def construct(self):
        # Create the box (business)
        # grid = NumberPlane()

        # self.add(grid)

        box = RoundedRectangle( width=3.0,
                               height=1.5,
                               corner_radius=0.1)
        box.move_to([0,2.5,0])

        # Create the text inside
        label = Text( "BUSINESS",
            font= "Poppins",
            font_size=27)

        # Center text inside box
        label.move_to(box.get_center())

        # Animation
        self.add(label)
        self.wait(2)

        # text
        t2 = Text("Bahan",
            font= "Poppins",
            font_size=27)
        t2.move_to([-4,1,0])

        self.add(t2)
        self.wait(2)

        t3 = Text("Equipment",
            font= "Poppins",
            font_size=27)
        t3.move_to([0,1,0])

        self.add(t3)
        self.wait(2)

        t4 = Text("Duit",
            font= "Poppins",
            font_size=27)
        t4.move_to([4,1,0])

        self.add(t4)
        self.wait(2)

        #Group kan semua ni then combine it into assets
        assets = VGroup(t2, t3, t4)

        t5 = Text("Asset",
            font= "Poppins",
            font_size=28,
            color = YELLOW,
            weight=BOLD)
        t5.move_to([0,1,0])

        self.play(Transform(assets, t5), run_time = 1.5)
        self.wait(1.5)
        
        t6 = MarkupText('Semua benda yang '
                        '<span foreground="yellow"><b>business ada</b></span> dan '
                        '<span foreground="yellow"><b>gunakan</b></span> '
                        '<span foreground="yellow"><b>untuk operation.</b></span>',
                        font="Poppins",
                        font_size=24)

        t6.next_to(assets, DOWN, buff=0.3)

        self.play(Write(t6), run_time=2)
        self.wait(2)

        # cross 
        cross = Line(
        start=assets.get_corner(UL),
        end=assets.get_corner(DR),
        color=RED)
        
        self.play(Create(cross))
        self.wait(0.5)

        cross2 = Line(
        start=t6[40:].get_corner(UL),
        end=t6[42:].get_corner(DR),
        color=RED)
        
        self.play(Create(cross2))
        self.wait(2)









