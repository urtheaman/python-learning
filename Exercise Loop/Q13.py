# Exercise Question 13: Write a loop to find the factorial of any number
def fac(n):
    res = 1
    if n>0:
        for i in range(1,n+1):
            res *= i
        return res
    else:
        print("It's only valid for +ve numbers.")

print(fac(6))
