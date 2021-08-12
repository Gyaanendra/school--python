k = int(input("enter the num :"))
a = 0
b = 0
c = 1
print(" here is fibnnoic sereis up to",k)
while a <=k:
    print(a)
    c = b+a
    a=b
    b=c
    a+=1      
