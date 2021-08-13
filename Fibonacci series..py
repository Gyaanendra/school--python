k = int(input("enter the num :"))
a = 0
b = 1
print(" here is fibnnoic sereis up to",k)
print(a)
for c in range(k):
    c = b+a
    a=b
    b=c
    print(a)    

