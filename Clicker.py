import turtle
import random
import time

# Set up the screen
wn = turtle.Screen()
wn.title("Click the Circles Game")
wn.bgcolor("white")
wn.setup(width=800, height=600)

# List to store the circles
circles = []
num_circles = 10
start_time = 0

# Function to create circles
def create_circle(x, y):
    circle = turtle.Turtle()
    circle.shape("circle")
    circle.color("red")
    circle.penup()
    circle.speed(0)
    circle.goto(x, y)
    return circle

# Function to place circles randomly
def place_circles():
    global start_time
    start_time = time.time()
    for _ in range(num_circles):
        x = random.randint(-300, 300)
        y = random.randint(-250, 250)
        circle = create_circle(x, y)
        circles.append(circle)

# Function to handle clicks
def click_handler(x, y):
    global num_circles
    for circle in circles:
        if circle.distance(x, y) < 20:  # Check if click is inside the circle
            circle.hideturtle()
            circles.remove(circle)
            num_circles -= 1
            if num_circles == 0:
                end_time = time.time()
                total_time = end_time - start_time
                print(f"Congratulations! You clicked all the circles in {total_time:.2f} seconds.")
                wn.bye()  # Close the turtle graphics window
            break

# Main game function
def main():
    place_circles()
    wn.onclick(click_handler)
    wn.mainloop()

# Run the game
if __name__ == "__main__":
    main()
