from manim import *

class scene4(MovingCameraScene):
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
            font_size=25,
            color=BLACK)
        
        # Center text inside box
        label.move_to(box.get_center())
        
        rect = SurroundingRectangle(label,
                                    color=BLACK,# border color
                                    fill_color=WHITE,   # fill white
                                    fill_opacity=1,
                                    buff=0.20)
        rect.round_corners(0.1)   

        # Animation
        self.add(rect, label)
        self.wait(2)
        
        arrow = Arrow(start=label,   # from box
                      end=[-3, 1, 0],             # target coordinate
                      buff=0,
                      color=TEAL_A,
                      tip_shape = ArrowCircleTip)
        
        arrow2 = Arrow(start=label,   # from box
                      end=[3, 1, 0],             # target coordinate
                      buff=0,
                      color=BLUE_A,
                      tip_shape = ArrowCircleTip)
        
        self.play(Create(arrow))

        self.wait(2)

        # Equity
        t1 = Text("Owner",
                  font= "Poppins",
                  weight=BOLD,
                  font_size=28,
                  color = TEAL_A)
        t1.move_to([-3,0.45,0])
        self.play(Write(t1))
        self.wait(1.5)

        t2 = Text("- Pemilik Syarikat masukkan duit \n   ke dalam business.",
                  font= "Poppins",
                  font_size=22,
                  color = TEAL_A,
                  line_spacing=1)
        t2.next_to(t1, DOWN, buff=0.4)
        self.play(Write(t2))
        self.wait(1.5)

        # Owner = Equity
        t3 = Text("Owner (Equity)",
                  font= "Poppins",
                  weight=BOLD,
                  font_size=28,
                  color = TEAL_A)
        t3[5:].set_color(TEAL_D)
        t3.move_to([-3,0.45,0])
        self.play(TransformMatchingShapes(t1, t3))
        self.wait()

        #arrow showing masukkan 10k
         
        # Dashed line
        dashed_line = Line(
            start=[-4.5, 2.5, 0],
            end=[0, 2.5, 0],
            color=TEAL_A)

        self.play(Create(dashed_line))
        self.wait(2)

        # aku nak add business and box sebab nak zoom nanti

        kita = Text("OWNER",
            font= "Poppins",
            font_size=25,
            color=BLACK)
        kita.move_to([-5,2.5,0])

        rect1 = SurroundingRectangle(kita,
                                    color=BLACK,# border color
                                    fill_color=WHITE,   # fill white
                                    fill_opacity=1,
                                    buff=0.20)
        rect1.round_corners(0.1)  
        
        self.add(rect, label)
        self.wait(2)

        # 10k along the line
        t4 = Text("RM10,000",
                  font= "Poppins",
                  weight=BOLD,
                  font_size=20,
                  )
        t4.move_to([-3,2.8,0])
        self.play(Write(t4))
        self.wait()

        
        #zoom dekat owner dengan
                
        self.play(self.camera.frame.animate.move_to([-1.5, 2.3, 0]).scale(0.7),
                     run_time=1.5)
        self.wait(1.5)
        self.add(rect1, kita)
        self.wait(1.5)
        
        # create a line that shows seperate entity
        dashed_line1 = DashedLine(
            start=[-2, 3.2, 0],
            end=[-2, 1, 0], 
            dash_length=0.1,
            color=YELLOW)
        
        self.play(Create(dashed_line1))
        self.wait(2)

        #seperate entity brace
        brace = BraceBetweenPoints(rect1.get_top(),
                                   rect.get_top(),
                                   direction=UP,
                                   buff = 0.5,
                                   color = YELLOW)
        
        brace.set_stroke(width=1)

        self.play(FadeIn(brace), run_time = 2) 
        self.wait(2)

        #seperate entity wording
        t5 = Text("Seperate Entity",
                  font= "Poppins",
                  weight=BOLD,
                  font_size=20,
                  color=YELLOW
                  )
        t5.next_to(brace, UP * 0.5)
        self.play(Create(t5))
        self.wait(1.5)

        #duit owner
        t6 = Text("Duit Owner",
                  font= "Poppins",
                  weight=BOLD,
                  font_size=20,
                  color=YELLOW
                  )   
        
        t6.move_to([-3,2.2,0])
        self.play(Write(t6))
        self.wait(1.5)
        
        # Duit Owner to Claim
        t7 = Text("Claim",
                  font= "Poppins",
                  weight=BOLD,
                  font_size=20,
                  color = YELLOW
                  )   
        
        t7.move_to([-3,2.2,0])
        self.play(Transform(t6, t7))
        self.wait(1.5)

        # camera zoom back bottom tunjuk owners equity

        self.play( self.camera.frame.animate.shift(DOWN * 2.5 + LEFT * 1),
                  run_time=1.5)
        self.wait(1.5)

        # camera keluar balik tapi zoom out sikit
             
        self.play(self.camera.frame.animate.move_to(ORIGIN + UP * 1.3).scale(1.37),
                  run_time=1.5)
                
        # original camera reset
        # self.play(
            # Transform(self.camera.frame, original_frame),
            # run_time=1.5)

        # Now Liability
        self.play(Create(arrow2))
        self.add(rect, label)
        
        self.wait(1.5)

        t8 = Text("Pinjaman",
                  font= "Poppins",
                  weight=BOLD,
                  font_size=28,
                  color = BLUE_A)
        t8.move_to([3,0.45,0])
        self.play(Write(t8))
        self.wait(1.5)
        
        # bank supplier 
        t9 = Text("- Third Party: Bank, Supplier \n   or Creditor.",
                  font= "Poppins",
                  font_size=22,
                  color = BLUE_A,
                  line_spacing=1)
        t9.next_to(t8, DOWN, buff=0.3)
        self.play(Write(t9))
        self.wait(1.5)

        # pinjam 5k
        bank = Text("BANK",
            font= "Poppins",
            font_size=25,
            color=BLACK)
        bank.move_to([5,2.5,0])

        rect3 = SurroundingRectangle(bank,
                                    color=BLACK,# border color
                                    fill_color=WHITE,   # fill white
                                    fill_opacity=1,
                                    buff=0.20)
        rect3.round_corners(0.1)
        
        #Duit 5k        
        t11 = Text("RM5,000",
                  font= "Poppins",
                  weight=BOLD,
                  font_size=20,
                  )
        t11.move_to([3,2.8,0])        

        dashed_line1 = Line(
            start=[4.5, 2.5, 0],
            end=rect.get_right(),
            color=BLUE_A)
        
        
        self.play(Create(dashed_line1),Write(t11), run_time = 1.2)
        self.add(rect3, bank)
        self.wait(2)

        # korang kena ingat
        self.play(self.camera.frame.animate.shift(RIGHT * 2.8),
                  run_time=1.5)
        self.wait(1.5)

        arrow6 = Arrow(t11.get_top() + UP * 0.9,
                       t11.get_top(),
                       color = YELLOW)
        self.play(Create(arrow6))
        self.wait(1.5)

        # bayar balik
        t12 = Text("Bayar Balik",
                  font= "Poppins",
                  weight=BOLD,
                  font_size=20,
                  color = YELLOW
                  )         
        t12.move_to([3,2.2,0])
        self.play(Write(t12))
        self.wait(1.5)

        # Tanggungjawab
        t13 = Text("Tanggungjawab untuk Bayar",
                  font= "Poppins",
                  weight=BOLD,
                  font_size=20,
                  color=YELLOW
                  )
        t13.next_to(arrow6, UP * 0.5)
        self.play(Create(t13), run_time = (2))
        self.wait(1.5)

        
        
        t10 = Text("Pinjaman (Liability)",
                  font= "Poppins",
                  weight=BOLD,
                  font_size=28,
                  color = BLUE_A)
        t10[8:].set_color(BLUE_B)
        t10.move_to([3,0.45,0])
        self.play(TransformMatchingShapes(t8, t10))
        self.wait(1.5)

        # camera back
        self.play(self.camera.frame.animate.shift(LEFT * 2.8),
                  run_time=1.5)
        self.wait(1.5)

        # Total assets
        t14 = Text("RM15,000",
                  font= "Poppins",
                  weight=BOLD,
                  font_size=23,
                  )
        t14.next_to(rect, DOWN, buff = 0.4)

        #groupkan 10k +5k
        source = VGroup(t4, t11)

        #camtumm
        self.play(TransformFromCopy(source, t14))
        self.wait(1.5)

        #highlight
        self.play(ShowPassingFlash(SurroundingRectangle(t14), run_time=1))
        self.wait(2)

        #create black box as if fade

        
        black_box = Rectangle(width=config.frame_width,
                              height=config.frame_height,
                              fill_color=BLACK,
                              fill_opacity=1,
                              stroke_width=0)
        self.play(FadeIn(black_box), run_time=1)
        self.wait(2)
