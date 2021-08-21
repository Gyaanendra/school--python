i = int(input("enter the number:"))

for n in range(2,i-1):
    if i%n ==0:
        print("not prime")
        break

else:
    print("prime")