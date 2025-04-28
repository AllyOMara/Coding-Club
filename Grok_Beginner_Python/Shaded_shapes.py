from turtle import

# Colours setup
bgcolor('skyblue')
fillcolor('royalblue')
pensize(7)
pencolor('mediumblue')
side_number = int(input("How many sides? "))

# Finding out how much to turn after each side is drawn
turn_angle = 360 / side_number

begin_fill()

# For loop to create the whole shape
for i in range(side_number):
  forward(45)
  left(turn_angle)

# Fills the shape with colour
end_fill()
