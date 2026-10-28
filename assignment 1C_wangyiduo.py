# Name: [Wang Yiduo]
# Assignment One task 3

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
