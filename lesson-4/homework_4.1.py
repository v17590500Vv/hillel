numbers = [1, 0, 2, 0, 0, 9, 3]
zero_count = numbers.count(0)
numbers = [num for num in numbers if num != 0]
numbers.extend([0] * zero_count)
print(numbers)