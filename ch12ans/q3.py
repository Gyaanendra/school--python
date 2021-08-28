'''
q3 pg 148
zsd
'''

s = input("enter a string: ")
if s[0] == "a" and len(s) <10 :
       print(s)

while len(s) <10:
    s =input("enter a string: ")
    if s[0] == "a"and len(s) <10 :
       print(s)
    elif len(s) <10:
        s =input("enter a string: ")
        if s[0] == "a"and len(s) <10 :
            print(s) 

