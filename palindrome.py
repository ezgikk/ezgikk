def palindromkelime (string):
    return string[::-1]==string
word=input()
if palindromkelime(word):
    print("{} palindromdur.".format(word))
else:
    print("palindrom değildir.")
