'''
# q5 pg 14b code
'''
mks=int(input("Enter you marks :"))
if mks>80:
    if mks>90:
        print("You win a prize of 2000/-")
    else:
        print("You wine  a prize of 1800")
elif mks>68:
    if mks>=80:
        print("You win a prize of 1500")
    else:
        print("You win a prize of 1400")
elif mks>60:
    print("You win a prize of 800")
else:
     print("sorry no gift")