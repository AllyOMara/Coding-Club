from turtle import

# Defines the function dandelion
def dandelion(x, y, length):
  penup()
  goto(x, -150)
  pendown()
  pensize(3)
  pencolor('#91F485')
  goto(x, y)
  angle = 360/40
  for i in range(20):
    pencolor("#0085C7")
    forward(length)
    goto(x, y)
    left(angle)
    pencolour("#009F3D")
    forward(length)
    goto(x, y)
    left(angle)

# Drawing the flowers
bgcolor('#ECFAF5')
dandelion(-0, 50, 60)
dandelion(-150, 40, 50)
dandelion(80, 50, 80)
