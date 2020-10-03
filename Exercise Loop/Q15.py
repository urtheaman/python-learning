# Exercise Question 15: Use a loop to display elements from a given list
# which are present at even positions
# Given:
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# for item in range(len(my_list)):
#     # for i in my_list:
#     if item % 2 != 0:
#         print(my_list[item], end=" ")

for i in my_list[1::2]:
    print(i)