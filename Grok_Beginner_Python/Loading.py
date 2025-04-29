from turtle import *

# Defining the draw_line function
def draw_line(value):
  red = value
  green = value
  blue = value
  pencolor(red, green, blue)
  pensize(8)
  penup()
  forward(30)
  pendown()
  forward(40)
  penup()
  goto(0, 0)

# Defining the load_indicator function
def load_indicator(num_lines):
  colour_value = 0
  angle = 360 / num_lines
  for i in range(num_lines):
    draw_line(colour_value)
    left(angle)
    colour_value = colour_value + 20

# Testing
load_indicator(13)
