# Name: [Wang Yiduo]
# Assignment One 

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


print("Question Answering Bot")
print("Type exit to leave the process")
ask=1
while ask==1:
	question = input("Ask me something: ")
	if question == "hello":
	    print("Bot: Hello! Nice to meet you.")
	elif question == "python":
	    print("Bot: Python is a language.")
	elif question == "HKU":
	    print("Bot: HKU is a university in HK")
	elif question == "human":
	    print("Bot: human created me")		
	elif question == "jetson":
	    print("Bot: Jetson Nano is an AI computer.")
	elif question == "ai":
	    print("Bot: AI means Artificial Intelligence.")
	elif question == "robot":
	    print("Bot: I am a chat robot")	
	elif question == "name":
	    print("Bot: My name is Python Bot.")
	elif question =="exit":
	    print("exit now")
	    ask=0
	else:
	    print("Bot: Sorry, I don't understand.")

print("Simple Calculator")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Choose operation (+, -, *, /): ")
if op == "+":
  print("Result:", num1 + num2)
elif op == "-":
  print("Result:", num1 - num2)
elif op == "*":
  print("Result:", num1 * num2)
elif op == "/":
  print("Result:", num1 / num2)
else:
  print("Invalid operation") 

