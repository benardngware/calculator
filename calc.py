def calculate(num1, num2, operator):
    if operator =="+":
        return num1 + num2
    elif operator =="-":
        return num1 - num2
    elif operator =="*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Cannot divide by zero"
        else :return num1/num2
    else:
        return "invalid operator"

num1 = float(input("first:"))
num2 = float(input("second:"))
operator = input("operator:")

result = calculate(num1, num2, operator)
print("Result:", result)
