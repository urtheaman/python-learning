# Exercise Question 11: Python program to display all the prime
# numbers within a range
start,end = input("Enter The Range : ").split()
for i in range(int(start),int(end) + 1):
    if i>1:
        for item in range(2,i):
            if i % item == 0:
                break
        else:
            print(i)
# Range = (5,11)
