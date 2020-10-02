# def stars(num,bool):
#     if bool == True:
#         for i in range(num):
#             for item in range(i+1):
#                 print("*", end=" ")
#             print("\n")
#     elif bool == False:
#         for i in range(num):
#             for item in range(num-i):
#                 print("*", end=" ")
#             print("\n")
#
#     return stars

def stars(num,bool):
    if bool == True:
        for i in range(num+1):
            print("* "*i)
    elif bool == False:
        for i in range(num,0,-1):
            print("* "*i)

    return stars

stars(7, 0)