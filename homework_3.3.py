box = [1, 21, 31, 41, 51, 61]
middle_index = (len(box) + 1) // 2
first_half = box[:middle_index]
second_half = box[middle_index:]
new_box = [first_half] + [second_half]
print(new_box)
