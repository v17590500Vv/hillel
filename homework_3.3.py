box1 = [1, 21, 31, 41, 51, 61]
change1_in_the_box1 = box1 [:3]
change2_in_the_box1 = box1 [-3:]
new_box1 = [change1_in_the_box1] + [change2_in_the_box1]
print(new_box1)

box2 = [99]
change1_in_the_box2 = box2 [:1]
change2_in_the_box2 = box2 [:0]
new_box2 = [change1_in_the_box2] + [change2_in_the_box2]
print(new_box2)

box3 = []
change1_in_the_box3 = box3 [:0]
change2_in_the_box3 = box3 [:0]
new_box3 = [change1_in_the_box3] + [change2_in_the_box3]
print(new_box3)