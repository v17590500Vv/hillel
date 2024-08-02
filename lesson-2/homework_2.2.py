number = int(input("Введіть 5-ти значне число: "))

first_digit = number // 10000
second_digit = (number % 10000) // 1000
third_digit = (number % 1000) // 100
fourth_digit = (number % 100) // 10
fifth_digit = number % 10

reversed_number = (fifth_digit * 10000 +
                   fourth_digit * 1000 +
                   third_digit * 100 +
                   second_digit * 10 +
                   first_digit)

print(reversed_number)