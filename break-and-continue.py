# i = 0
#
# while(True):
#     if i < 5:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 45:
#         break
#     i += 1

#Quiz


while(True):
    var = int(input("Enter Your No. "))
    if var<100:
        continue
    elif var>100:
        print("Greater Than 100")
        break
    else:
        print("Equal To 100")
        break
