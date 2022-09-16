def palindromenumber(x):
    temp=x
    rev=0
    while x > 0:
        digit =x % 10
        rev = rev * 10 + digit
        x = x // 10
    return rev==temp

num=int(input())
if palindromenumber(num):
    print("palindrome")
else:
    print("it's not palindrome ")
