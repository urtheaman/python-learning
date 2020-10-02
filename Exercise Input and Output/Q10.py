# Exercise Question 10: Read line number 4 from the following file
with open("Q10 test.txt") as f:
    # for n,line in enumerate(f):
    #     if n+1 == 4:
    #         print(line)

    print(f.readlines()[3])
