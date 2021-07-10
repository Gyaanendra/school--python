# calculator program
a = int(input("Enter num1:"))
b = int(input("Enter num2:"))
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
choice= int(input("Enter num:"))

# calculation
if choice == 1:
    c=a+b
    print("Addition:",c)
elif choice == 2:
     d=a-b 
     print("Subtraction:",d)
elif choice == 3:
   e=a*b 
   print("Multilpy:",e) 
elif choice == 4:
    f=a/b
    print("divide:",f)   
else:
    print('invalid')

  



