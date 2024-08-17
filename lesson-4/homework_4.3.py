import random

length = random.randint(3, 10)
numbers = [random.randint(1, 10) for _ in range(length)]
if length >= 3:
    new_list = [numbers[0], numbers[2], numbers[-2]]

print("First list :", numbers)
print("Second list:", new_list)