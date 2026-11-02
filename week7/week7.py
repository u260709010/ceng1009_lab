#        # Exercise 1
#
#  def sumTo(n):
#      return(int((n*(n+1))/2))
#  n = int(input("Please enter a number: "))
#  print(sumTo(n))
# mport turtle
# rom encodings import undefined
#
#
#        # Exercise 2
#
#  import turtle
#  tur = turtle.Turtle()
#  screen = turtle.Screen()
#  def drawStar(tur,n,size):
#      angle = 180 - 180 / n
#      for i in range(n):
#          tur.forward(size)
#          tur.right(angle)
#  drawStar(tur,5,100)
#  screen.exitonclick()
#
#        #Exercise 3
#
#  def sumTo(n):
#      total = 0
#      for i in range(1, n+1):
#          total += i
#      return total
#  n = int(input("Please enter a number: "))
#  print("Sum is: ", sumTo(n))
#
#         #Exercise 4
#
#  import math
#  def mySqrt(n):
#      execute = n/2
#      for i in range(20):
#          execute = (1/2) * (execute + n/execute)
#      return execute
#  print("The result is ",mySqrt(100))
#  print("The result is ", math.sqrt(100))
#
#        #Exercise 5
#
#  import turtle
#  tur = turtle.Turtle()
#  screen = turtle.Screen()
#  def drawSprite(tur, legs, length):
#      angle = 360/legs
#      for i in range(legs):
#          tur.forward(length)
#          drawTip(tur, 10)
#          tur.backward(length)
#          tur.left(angle)
#  def fancySquare(tur, size):
#      for corner in range(4):
#          drawSprite(tur, 8, 28)
#          tur.forward(size)
#          tur.left(90)
#  def drawTip(tur, size):
#      tur.begin_fill()
#      tur.left(90)
#      tur.forward(size/2)
#      tur.right(120)
#      tur.fd(size)
#      tur.right(120)
#      tur.fd(size)
#      tur.right(120)
#      tur.fd(size/2)
#      tur.right(90)
#      tur.end_fill()
#  def spriteTip(tur, size):
#      for corner in range(4):
#          drawSprite(tur, 8, 20)
#          tur.forward(size)
#          tur.left(90)
#
#  tur.color("pink")
#  tur.pensize(1)
#  tur.speed(10)
#  fancySquare(tur, 100)
#  screen.exitonclick()
#
#        #Exercise 6
#
#  def checkSign(x):
#      if x > 0:
#          return "The number is positive"
#      elif x < 0:
#          return "The number is negative"
#      else:
#          return "The number is zero"
#  numbers = [-7, 5, 0]
#  for number in numbers:
#      print(checkSign(number))
#
#         #Exercise 7
#
#  tur = turtle.Turtle()
#  screen = turtle.Screen()
#  def drawBar(tur, height, gap):
#      tur.penup()
#      tur.left(90)
#      tur.forward(height + gap)
#      tur.write(" " + str(height))
#      tur.backward(height + gap)
#      tur.right(90)
#      tur.pendown()
#
#      tur.begin_fill()
#      tur.left(90)
#      tur.forward(height)
#      tur.right(90)
#      tur.forward(40)
#      tur.right(90)
#      tur.forward(height)
#      tur.left(90)
#      tur.end_fill()
#  def BarChart():
#      maxheight = max(data)
#      num_bars = len(data)
#      border = 10
#
#      gap = (maxheight - border) / 25
#
#      right = 40 * num_bars + border
#      top = maxheight + 4 * border
#      screen.setworldcoordinates(-border, -border, right, top)
#      tur.color("blue")
#      tur.fillcolor("red")
#      tur.pensize(3)
#      for height in data:
#          drawBar(tur, height, gap)
#  data = [48, 117, 200, 240, 160, 260, 220]
#  BarChart()
#  screen.bgcolor("lightgreen")
#  screen.exitonclick()
#  screen.exitonclick()