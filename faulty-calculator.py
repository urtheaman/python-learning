# 12*45=56, 45/12=2, 85-47=15, 45+12=25

print("Enter Your First Desired Number:")
num1 = int(input())
print("Enter Your Second Desired Number:")
num2 = int(input())
print("Which Function Do You Want To Use ?\n1. Addition (+)\n2. Subtraction (-)\n3. Multiply(*)\n4. Divide(/)")
print("Type B/w 1 - 4:")
while(True):
    key = int(input())
    if key == 1:
        result = num1 + num2
        if num1 == 45 and num2 == 12 or num1==12 and num2==45:
            result = 25
        break
    elif key==2:
        result = num1 - num2
        if num1==85 and num2==47:
            result = 15
        break
    elif key==3:
        result = num1 * num2
        if num1==12 and num2==45 or num1==45 and num2==12:
            result=56
        break
    elif key==4:
        result = num1 / num2
        if num1==45 and num2==12:
            result=2
        break
    else:
        print("Sorry! Please Choose B/w 1 - 4 Only")
        continue
print(result)
