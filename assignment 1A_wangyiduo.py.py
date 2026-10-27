# Name: [Wang Yiduo]
# Assignment One task 1

import turtle

# Set up the screen and window background
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Dynamic Colorful Star Pattern")

# Initialize the turtle
t = turtle.Turtle()
t.speed(0)  # Maximum drawing speed
t.width(2)

# Define a palette of vibrant colors
colors = ["#FF5733", "#33FF57", "#3357FF", "#F3FF33", "#FF33F3", "#33FFF3"]

# Number of iterations for our pattern
num_steps = 150

# Incorporate a structured for loop for the dynamic pattern
for i in range(num_steps):
  # Dynamically change the pen color using modulo to cycle through the list
  t.pencolor(colors[i % len(colors)])

  # Dynamically change the length as the loop progresses (creates a spiral effect)
  t.forward(i * 2.5)

  # Turn the turtle at an angle that forms a multi-pointed star
  t.right(144)

# Clean up and finish
t.hideturtle()
turtle.done()
