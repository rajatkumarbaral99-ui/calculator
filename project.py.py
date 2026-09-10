print("Simple Calculator")

num1 = float(input("Pehla number enter karo: "))
operator = input("Operator enter karo (+, -, *, /): ")
num2 = float(input("Dusra number enter karo: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 -num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: 0 se divide nahi kar sakte!"
else:
    result = "Invalid operator!"

print("Result:", result)
