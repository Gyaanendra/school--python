'''
program is to find hcf and lcm of two no.
'''
num1 = int(input("enter the first no:"))
num2 = int(input("enter the second no:"))

'''
finding hcf first 
'''
if num2 > num1:
    mn = num1
else:
    mn = num2


for i in range(1, mn+1):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i

print("the hcf of the two numbers:", hcf)

'''
finding lcm
'''
lcm = (num1*num2)/hcf
print("the lcm of the two numbers:", lcm)
