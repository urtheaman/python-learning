i=0
while(i<9):
    leftGuesses = 9 - i
    print("No. Of Guesses Left: ", leftGuesses)
    num = 18
    print("Guess The No. Which is Hidden")
    guess = int(input())

    if guess==num:
        print("Congrats! You Got It.")
        print("You Took ",i," Guesses To Complete It.")
        break
    elif num-1<=guess<=num+1:
        print("You Are Most Likely To Get It.")
    elif num-2<=guess<=num+2:
        print("You are Very Likely to guess it.")
    elif num-5<guess<num+5:
        print("You are about to Guess it.")
    elif num-10<guess<num+10:
        print("You are trying it.")
    else:
        print("You are not trying well.")
    i += 1
print("Game Over")
