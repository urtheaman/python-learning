url = 'https://pynative.com/python-basic-exercise-for-beginners/'

# Question 1: Given a two integer numbers return their product and  if the product is greater than 1000, then return their sum

# # ---------------------------------------------
# def fun1(a,b):
#     if a * b<=1000:
#         print("Your Product Is ", a * b)
#     else:
#         print("The Sum Is ", a + b)
#     return fun1
# # ---------------------------------------------
# num1 = 30
# num2 = 20
# print(fun1(num1,num2))
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Question 2: Given a range of first 10 numbers, Iterate from start computer_number to the end computer_number and print the sum of the current computer_number and previous computer_number

# # -------------------------------------------------------------------------------
# def SumNum(num):
#     prevNum = 0
#     for i in range(num):
#         print("Current No.: ", i, "Previous No.: ", prevNum, "Sum Is: ", i+prevNum)
#         prevNum = i

#     return SumNum
# # ----------------------------------------------------------------------------------
# SumNum(10)
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Question 3: Given a string, display only those characters which are present at an even index computer_number.
"""Method 1 (List Method)"""
# # ---------------------------------------------------------
# def string_slicing_even(string):
#     list1 = []
#     for i in string:
#         list1.append(i)
#     print(list1[::2])

#     return string_slicing_even
# # -----------------------------------------------------------

# string_slicing_even("AmandaCerny")

"""Method 2 (Range Method)"""
# # ------------------------------------------------------------
# def evenChars(str):
#     print("Orginal String is ", str)
#     print("Printing only even index chars...")
#     for i in range(0, len(str), 2):
#         print('at', i, str[i])

#     return evenChars
# # -----------------------------------------------------------
# evenChars("pynative")
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Question 4. Given a string and an integer computer_number n, remove characters from a string starting from zero up to n and return a new string

# # ------------------------------------------------------------
# def removestring(str,n):
#     if n<len(str):
#         # newstr = str.replace(str[0:n+1],"")  
#         newstr = str[n+1:]
#         print("New String Is: ",newstr)
#     else:
#         print("Plz Reduce The Number n Value")
# # -----------------------------------------------------------
# removestring("pynative",5)
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Question 5: Given a list of numbers, return True if first and last computer_number of a list is same

# # ------------------------------------------------------------
# def checkList(list):
#     print("Given list is ", list)
#     if list[0] == list[-1]:
#         print("result is True")
#     else:
#         print("result is False")
#     return checkList
# # ------------------------------------------------------------
# list1 = [10, 20, 30, 40, 10]
# list2 = [10, 20, 30, 40, 50]
# checkList(list1)
# checkList(list2)
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Question 6: Given a list of numbers, Iterate it and print only those numbers which are divisible of 5

# # -------------------------------------------------------------
# def divisibleby5(givenlist):
#     print("Numbers In The List Which Are Divisible By 5:")
#     for i in givenlist:
#         if i % 5 == 0:
#             print(i)
#
#     return divisibleby5
# # ------------------------------------------------------------
# list1 = [10, 20, 30, 49, 50]
# divisibleby5(list1)
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Question 7: Return the total count of sub-string “Emma” appears in the given string

# e,m,a
# em,ea,me,ma,mm,am,ae
# emm,ema,eam,

# # ------------------------------------------------------------
# def totalcount(sentence,str):
#     print(sentence.count(str))
#
#     return totalcount
# # -----------------------------------------------------------
# totalcount("Emma is good developer. Emma Emma is a writer","Emma")

"""Method 2 (Without using string function count)"""
# def totalcount(sentence,str):
#     count = 0
#     for i in range(len(sentence)):
#         if sentence[i: (i+len(str))] == str:
#             count += 1
#     print(count)
#
#     return totalcount
#
# totalcount("Emma is good developer. Emma Emma is a writer","Emma")
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Question 8: Print the following pattern
# --------------------------------------------------
# def printpattern(num):
#     for i in range(num+1):
#         for item in range(i):
#             print(i, end=" ")
#         print("\n")
#
#     return printpattern
# ---------------------------------------------------
# printpattern(5)
# //////////////////////////////////////////////////////////////////////////////////////////////////

# Question 9: Reverse a given computer_number and return true if it is the same as the original computer_number

# # --------------------------------------------------
# def reverse(num):
#     revNum = 0
#     givenNum = num
#     print("Original No. ", givenNum)
#     while(givenNum>0):
#         reminder = givenNum % 10
#         givenNum = givenNum // 10
#         revNum = revNum * 10 + reminder
#     print("Reversed No. ", revNum)
#     if num == revNum:
#         print("The original and reverse computer_number is the same")
#     else:
#         print("The original and reverse computer_number is not same")
#
#     return reverse
# # -------------------------------------------------------
# reverse(121)
# //////////////////////////////////////////////////////////////////////////////////////////////////

# Question 10: Given a two list of numbers create a new list such that new list should contain only odd numbers from the first list and even numbers from the second list

# # -------------------------------------------------------
# def oddEvenPicker(list1,list2):
#     list3 = []
#     for i in list1:
#         if i % 2 == 0:
#             list3.append(i)
#     for item in list2:
#         if item % 2 != 0:
#             list3.append(item)
#     print(list3)
#
#     return oddEvenPicker
# # -------------------------------------------------------
# oddEvenPicker([10, 20, 23, 11, 17],[13, 43, 24, 36, 12])
# //////////////////////////////////////////////////////////////////////////////////////////////////

# Question 11: Write a code to extract each digit from an integer, in the reverse order

# # -------------------------------------------------------
# def extractdigit(num):
#     num = str(num)
#     i = len(num)-1
#     while(i>=0):
#         print(num[i], end=" ")
#         i -= 1
#
#     return extractdigit
# # -------------------------------------------------------
# # -------------------------------------------------------
# def extract(num):
#     givennum = num
#     while(givennum>0):
#         reminder = givennum % 10
#         givennum = givennum // 10
#         print(reminder, end=" ")
#
#     return extract
# # -------------------------------------------------------
# extract(7536)
# //////////////////////////////////////////////////////////////////////////////////////////////////

# Question 12: Calculate income tax for the given income by adhering to the below rules

# Taxable
# Income
# Rate( %)
# First $10, 000
# 0
# Next $10, 000
# 10
# The
# remaining
# 20

# # -------------------------------------------------------
# def incomeTax(income):
#     if income<=10000:
#         tax = 0
#     elif income<=20000:
#         tax = (income - 10000) * 10 / 100
#     else:
#         tax = 0
#         tax += 10000 * 10 / 100
#         tax += (income - 20000) * 20 / 100
#     print("Total Payable Tax: ", tax)
#
#     return incomeTax
# # -------------------------------------------------------
# incomeTax(19000)
# //////////////////////////////////////////////////////////////////////////////////////////////////

# Question 13: Print multiplication table form 1 to 10
# # -------------------------------------------------------
# def table(num):
#     for i in range(1,num+1):
#         for item in range(1,11):
#             print(i * item, end=" ")
#         print("\n")
#
#     return table
# # # -------------------------------------------------------
# table(12)
# //////////////////////////////////////////////////////////////////////////////////////////////////

# Question 14: Print downward Half-Pyramid Pattern with Star (asterisk)
# # # -------------------------------------------------------
# def halfPyramid(num):
#     for i in range(num):
#         for item in range(num-i):
#             print("*", end=" ")
#         print("\n")
#
#     return halfPyramid
# # # -------------------------------------------------------
# halfPyramid(5)
# //////////////////////////////////////////////////////////////////////////////////////////////////

# Question 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
# # # -------------------------------------------------------
# def exponent(base, exp):
#     result = 1
#     for i in range(exp):
#         result *= base
#     print(base, " To The Power ",exp, " = ",result)
#
#     return exponent
# # # # -------------------------------------------------------
# exponent(2,5)
# //////////////////////////////////////////////////////////////////////////////////////////////////

