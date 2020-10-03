# Exercise Question 8: Reverse the following list using for loop
list1 = [10, 20, 30, 40, 50]
length = len(list1)
for i in range(length,0,-1):
    print(list1[i-1])
