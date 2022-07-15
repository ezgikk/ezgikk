answer = 5
print("please guess number between 1 and 10.")
guess=int(input())
if guess==answer:
    print("YOU have guessed first time.")
else:
    if guess<answer:
        print("guess higher.")
        guess = int(input())
    else:
        print("guess lower")
        guess = int(input())
    if guess==answer:
        print("you have guessed correctly")
    else:
        print("sorry,you haven't guessed correctly")
