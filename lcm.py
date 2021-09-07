'''
program is to find hcf and lcm of two no.
'''


num1 = int(input("enter the first no:"))
num2 = int(input("enter the second no:"))

'''
find lcm first 
'''
for m in range(1, num1*num2+1):
    if m % num1 == 0 and m % num2 == 0:
        lcm = m

print("the lcm of the two numbers:", lcm)

'''
finding hcf
'''
hcf = int((num1*num2)/lcm)
print("the hcf of the two numbers:", hcf)
