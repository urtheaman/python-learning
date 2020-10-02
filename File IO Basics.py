# No Volatile Memory - Hard Disk Memory , Which Does Not change or removes without user permission, which exists until user deletes the file.

# "r" = Open File for reading
# "w" = Open File for writing
# "x" = Creates File if does not exist
# "a" = Append something in file  / Add More Content To A File
# "t" = Text Mode
# "b" = binary mode
# "+" = read and write both at the same time
#
# file = open("text.txt", "r+")
# content = file.writable()
# print(content)
#
# content = file.read()
# print(content)
# file.close()
#
# file = open("aman.txt", "a")
# a = file.write("I am Aman.\n")
# print(a)
# file.close()

# i = 9
# while i>0:
#     file = open("aman.txt", "r+")
#     content = file.read()
#     print(content)
#     file.write("TheAman \n")
#     file.close()
#     i -= 1

# Tell and seek functions
# f = open("text.txt")
# f.seek(10)
# print(f.tell())
# print(f.readline())
# f.seek(1)
# print(f.tell())
# print(f.read())

# def fun1(func):
#     for i in func:
#         print(i, end="||")
#
#     return fun1
#
# f = open("text.txt")
# fun1(f)
# f.close()

# # Using With Block To Open PYTHON FILES
# # with open("aman.txt") as f:
# #     a = f.read()
# #     # a = a.replace("\n", "")
# #     print(a)

