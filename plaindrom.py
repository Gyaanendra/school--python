#inputing a string from user 
s = input("Enter the word:")
#reversing it 
rs = (s[::-1])

#checking if they are equal
if s == rs:
    print('it is a palindrome')
#if not 
else:
    print('it is not a palindrome')
