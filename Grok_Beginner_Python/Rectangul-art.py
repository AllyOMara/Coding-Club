from turtle import

# Defining the function draw_rect to draw a rectangle
def draw_rect(width, height, colour):
  pensize(3)
  colour = pencolour(colour)
  forward(width)
  left(90)
  forward(height)
  left(90)
  forward(width)
  left(90)
  forward(height)
  left(90)

# Drawing the buildings
draw_rect(30, 120, 'royalblue')
goto(-10, 0)
draw_rect(80, 30, 'cornflowerblue')
goto(-30, 0)
draw_rect(80, 60, 'coral')
goto(-45, 0)
draw_rect(50, 80, 'plum')
