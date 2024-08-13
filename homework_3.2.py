x = [10, 100, 200, 500, 5]
last_element = x [-1]
x [1:] = x [:-1]
x[0] = last_element
print(x)