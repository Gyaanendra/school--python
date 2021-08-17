s = input("Enter the word:")
rs = (s[::-1])

if rs == s:
    print('it is a palindrome')
else:
    print('it is not a palindrome')
