# Exercise Given by Harry

words = {'Computer': "A machine that helps human to do calculations easily",
         'Keyboard': "A hardware used to type things"}
inputText = input()
if inputText in words.keys():
    print(words[inputText])
else:
    print("Not able to fetch keys you entered")
