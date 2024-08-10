numbers1 = float(input("please enter a number: "))
numbers2 = float(input("please enter a number: "))
calculations = input("Please enter any of the available signs +, -, *, /: ")
if calculations == "+":
    result = numbers1 + numbers2
elif calculations == "-":
    result = numbers1 - numbers2
elif calculations == "*":
    result = numbers1 * numbers2
elif calculations == "/":
    if numbers2 != 0:
        result = numbers1 / numbers2
    else:
        result = "Error: Cannot divide by 0"
print("Result: ", result )




