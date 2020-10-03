# Exercise Question 14: Reverse a given integer number 546
integer = int(input("Enter Integer : "))
reverse = 0
while integer>0:
    reminder = integer % 10
    integer //= 10
    reverse = reverse*10 + reminder
print(reverse)