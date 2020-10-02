# Exercise Question 2: Print the following pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

def printer(num):
    for i in range(num):
        for item in range(i+1):
            print(item+1, end=" ")
        print()
    return printer

number = int(input("Enter no. : "))
printer(number)
