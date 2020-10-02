# print('%.2f' % 458.541315)

# Exercise Question 5: Accept list of 5 float numbers as a input from user
list1 = []
listlength = int(input("Enter your list length : "))
x = listlength
while x>0:
    num = float(input("Enter your float no. : "))
    list1.append(num)
    x -= 1
print(list1)
