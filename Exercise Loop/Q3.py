# Exercise Question 3: Accept number from user and calculate the sum of all number between 1 and given number
while True:
    sum1 = 0
    num = int(input("Enter No. : "))
    for i in range(1,num+1):
        sum1 += i
    print(sum1)
    restart = input("Press Any Key To Restart...")
    if restart.__str__():
        continue

