# This implements the circle class
import math
import turtle
class circle:
    def __init__(self, radius = None, color = None):
        if radius is None and color is None:   # default constructor
            self.__radius = 25
            self.__color = 'red'
        else:                               # parameterized constructor
            self.__radius = radius
            self.__color = color
            
    def __str__(self):
        return f'The current radius is {self.__radius:.2f}\n'\
               f'The current color is {self.__color}\n'
    
    def get_radius(self):
        return self.__radius
    
    def set_radius(self, radius):
        self.__radius = radius
        
    def get_color(self):
        return self.__color
    
    def set_color(self, color):
        self.__color = color
        
    def calc_area(self):
        return math.pi * self.__radius * self.__radius
    
    def calc_circum(self):
        return 2 * math.pi * self.__radius
    
    def draw_circle(self):
        turtle.pencolor(self.__color)
        turtle.circle(self.__radius)

    
        
