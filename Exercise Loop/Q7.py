# Exercise Question 7: Print the following pattern using for loop
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

num = int(input("Enter No. : "))
# for i in range(1,num+1):
#     for item in range(num+1-i,0,-1):
for i in range(num,0,-1):
    for item in range(i,0,-1):
        print(item, end=" ")
    print()

