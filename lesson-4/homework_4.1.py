numbers = [1, 0, 2, 0, 0, 9, 3]
for num in numbers[::-1]:
    if num == 0:
        numbers.remove(num)
        numbers.append(0)

print(numbers)