# Exercise Question 6: Given a number count the total number of digits in a number
num = 1425645
# x = str(num)
# print(len(x))

count = 0
while num != 0:
    num = num // 10
    count += 1
print(count)
