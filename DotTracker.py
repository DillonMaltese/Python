import turtle
yPos = 0
xPos = 0


def drag(x, y):
    # stop backtracking
    circle.ondrag(None)

    # go to x, y
    circle.goto(x, y)

    print("Circle is at ({0},{1})".format(x, y))

    # call again
    circle.ondrag(drag)


screen = turtle.Screen()
screen.setup(300, 400)
screen.bgcolor("black")
circle = turtle.Turtle()
circle.shape("circle")
circle.color("dark red")
circle.penup()
circle.speed(10)
circle.ondrag(drag)
screen.mainloop()
