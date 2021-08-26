'''
# qf part 2 pg 148 
# this program is to print prime number up to the user
#   inputed number
'''
u = int(input("Enter u range: "))  
cnt =1 


for num in range(1,u - 1):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           print(cnt,".",num)
           cnt+=1  


