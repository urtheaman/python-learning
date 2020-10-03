# Exercise Question 12: Display Fibonacci series up to 10 terms
def fibonacci(num):
    first_no = 0
    second_no = 1
    add = 0
    if num >= 2:
        for i in range(num):
            add = first_no + second_no
            if i == 0:
                add = 0
            first_no = second_no
            second_no = add
            print(add)
    else:
        print("Enter No. Greater Than 2.")
    return fibonacci
fibonacci(15)
