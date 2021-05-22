from manim import *
import numpy as np

class sine_curve_circle(Scene):
    def construct(self):
        #define axis and create
        ax = Axes(x_range = [-2,7],y_range = [-2,2], axis_config= {"include_numbers":"True","color":"#77c5f4"},y_length= 16/3, x_length = 12)
        self.play(Create(ax))



        #define circle on axis

        circle = Circle(radius = ax.coords_to_point(-1,0)[0]-ax.coords_to_point(0,0)[0]).move_to(ax.coords_to_point(-1,0))
        self.play(Create(circle))




        #define dot

        dot = Dot(radius = 0.1).move_to(ax.coords_to_point(0,0))
        def radial_line():
            return Line(circle.get_center(),dot.get_center(), color  = YELLOW)
        radius_constant = radial_line()
        self.play(Create(radius_constant))
        self.play(Create(dot))

        
        



        #define graph
        sine = ax.get_graph(lambda x:np.sin(x),x_range = [0,0], color = YELLOW)



        #updaters!

        self.displacement = 0
        self.rate = 0.1


        tracker = ValueTracker(0)

        def update_dot(obj,dt):
            self.displacement += (self.rate * dt) 
            obj.move_to(circle.point_from_proportion((self.displacement + 0.5) % 1))

        def update_graph(obj,dt):
            self.displacement += self.rate * dt
            obj.become(ax.get_graph(lambda x: np.sin(x),x_range = [0,self.displacement * 2 * np.pi], color = YELLOW))

        
        dot.add_updater(update_dot)
        

        sine.add_updater(update_graph)

         
            


        def radial_line():
            return Line(circle.get_center(),dot.get_center(), color  = YELLOW)

        

        radius = always_redraw(radial_line)
        
        
        
        #horizontal line

        horizontal_line = Line(dot.get_center(),np.array([0,0,0]),color = PURPLE)

        def update_horizontal_line(obj,dt):
            obj.become(Line(dot.get_center(),np.array([15,dot.get_center()[1],0]),color = PURPLE))

        horizontal_line.add_updater(update_horizontal_line)

       
            
        
        self.add(always_redraw(lambda : dot),always_redraw(lambda :sine),radius,horizontal_line)
        self.remove(radius_constant)

        self.wait(8)

        

        

        

        


        

        

    
