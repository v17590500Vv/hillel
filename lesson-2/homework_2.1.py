number = int(input("Введіть 4-х значне число: "))

first_digit = number // 1000
second_digit = (number % 1000) // 100
third_digit = (number % 100) // 10
fourth_digit = number % 10

print(first_digit)
print(second_digit)
print(third_digit)
print(fourth_digit)