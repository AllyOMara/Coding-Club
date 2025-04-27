from turtle import *

# Determines the number of sleepers to be created based on user input
sleeper_number = int(input("How many sleepers? "))

# Sets up turtle in the correct position
pencolour('gray')
pensize(10)
penup()
left(180)
forward(160)
left(180)
pendown()

# Makes as many sleepers as the user inputted
for i in range(sleeper_number):
  left(90)
  forward(100)
  right(180)
  forward(100)
  penup()
  left(90)
  forward(40)
  pendown()
