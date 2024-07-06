import turtle
import random
import time
# Fullscreen the canvas
screen = turtle.Screen()
screen.title("Turtle game")
screen.bgcolor("pink")
screen.setup(width=800,height=800)
circles=[]
numCircles=10
startTime=0

def createCircle(x,y):
  circle = turtle.Turtle()
  circle.shape("circle")
  circle.color("green")
  circle.penup()
  circle.speed(0)
  circle.goto(x,y)
  return circle

def placeCircles():
  global startTime
  startTime=time.time()
  for u in range(numCircles):
    x=random.randint(-300,300)
    y=random.randint(-250,250)
    circle=createCircle(x,y)
    circles.append(circle)

def clickHandler(x,y):
  global numCircles 
  for t in circles:
    if t.distance(x,y)<20:
      t.hideturtle()
      circles.remove(t)
      numCircles-=1
      if numCircles==0:
        endtime=time.time()
        totaltime=endtime-startTime
        print("You clicked all of the circles with the time of",totaltime)
        screen.bye()
      break

def main():
  placeCircles()
  screen.onclick(clickHandler)
  screen.mainloop()

if __name__=="__main__":
  main()