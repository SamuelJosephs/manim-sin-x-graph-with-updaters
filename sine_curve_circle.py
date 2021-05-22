from manim import *
import numpy as np


class graph(Scene):
    def construct(self):
        ax = Axes(x_range = [-2,7],y_range = [-2,3],axis_config = {"include_numbers":"True"})

        self.play(Create(ax))
        self.rate = 0.25
        self.end_point = 0.1
        def update_end_point(c,dt):
            rate = dt * 2 
            c.become(ax.get_graph(lambda x: np.sin(x), x_range = [0,self.end_point + rate],color = YELLOW))
            self.end_point += rate
            

        
            

        #make graph

        sine = ax.get_graph(lambda x: np.sin(x), color = YELLOW, x_range = [0,0])
    
        self.add(sine)
        sine.add_updater(update_end_point)
        self.add(sine)

        self.wait(3)

        #self.wait(4)

        # sine_graph = always_redraw(lambda : sine)

        # self.add(sine_graph)

        # self.play(sine_graph.animate.increment_value(2 * np.pi))

class test(Scene):
    def construct(self):
        ax = Axes(x_range = [-2,7],y_range = [-2,3],axis_config = {"include_numbers":"True"})
        sine = ax.get_graph(lambda x: np.sin(x), color = YELLOW, x_range = [0,2 * np.pi])
        self.play(Create(ax))
        self.play(Create(sine))

        

        

        

        

        


        

        

    
