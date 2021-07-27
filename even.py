# to print even number
N= int(input(" Please Enter any Maximum Value : "))

for n in range(N):
    if(n % 2 == 0):
        print(n)
        
if(N % 2 == 0):
    print(N)
