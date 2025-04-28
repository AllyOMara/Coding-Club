from turtle import

# Defining the function draw_petal
def draw_petal(colour):
  pencolor(colour)
  for i in range(4):
    forward(60)
    left(90)

# Pen and background setup
pensize(5)
bgcolor('lightgreen')
fillcolor('hotpink')

# Gets the petal number from the user's input
petal_number = int(input("How many petals? "))

# Finding the angle the turtle should turn
angle = 360 / petal_number

# Starts the fill
begin_fill()

# For loop to draw the number of petals based on user input (see above)
for i in range(petal_number):
  draw_petal('purple')
  left(angle)

# Ending the fill
end_fill()
