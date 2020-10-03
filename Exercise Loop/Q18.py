# Exercise Question 18: Print the following pattern
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
def printer(n):
    for i in range(n):
        for item in range(i+1):
            print("*", end=" ")
        print()

    for i in range(n,0,-1):
        for item in range(i):
            print("*", end=" ")
        print()
    return printer

printer(5)

# def printer(n):
#     for i in range(1,n+1):
#         print("* "*i)
#     for i in range(n,0,-1):
#         print("* "*i)
#     return printer
#
# printer(5)