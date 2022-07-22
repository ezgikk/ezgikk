print("please choose your option from the list below:")
print("1:\tLearn Python ")
print("2:\tLearn Java ")
print("3:\tGo swimming ")
print("4:\tHave dinner ")
print("5:\tGo to bed ")
print("0:\tExit ")
a=0

while a < 6:
    a = int(input("please choose 0 between 5:"))
    if a == 0:
        print("Game over")
        break

    elif a==1:
       print("you choosed {}. option".format(a))
    elif a==2:
       print("you choosed {}. option".format(a))
    elif a==3:
       print("you choosed {}. option".format(a))
    else:
        print("there is no option like that")
else:
    print("please choose your option from the list below:")
    print("1:\tLearn Python ")
    print("2:\tLearn Java ")
    print("3:\tGo swimming ")
    print("4:\tHave dinner ")
    print("5:\tGo to bed ")
    print("0:\tExit ")
a=int(input("please choose 0 between 5:"))
