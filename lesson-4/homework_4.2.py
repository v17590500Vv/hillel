numbers = [0, 1, 7, 2, 4, 8]
sum_even_indices = sum(numbers[i] for i in range(0, len(numbers), 2))
result = sum_even_indices * numbers[-1]
print(result)