#simple calculator
firstnumber = float(input("First Number:"))
secondnumber = float(input("Second number:"))
myoperator= str(input("Enter operator(+, -, /, *)"))


if myoperator== "+":
    print(firstnumber+secondnumber)
elif myoperator=="-":
    print(firstnumber-secondnumber)
elif myoperator=="*":
    print(firstnumber*secondnumber)
elif myoperator=="/":
    print(firstnumber/secondnumber)
else:
    print("Invalid Operator")


