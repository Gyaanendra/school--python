'''
program to find the minimum and maximum value of lists
'''

lst = [1, 45, 446, 576, 68, 7, 9, 54654, 2343, 21, 321312, 3123, 123, 123, 123, 0, 65776,
       8, 67, 6, 45654, 45, 6, 456, 4565, 6456, 886896, 35263, 346543534, 543, 5345, 34]
'''
 FIRST WAY is to print using min() and max() function
'''

print('THE FIRST WAY')
print(min(lst))
print(max(lst))


'''
second way is to first sort the list and print [0], [-1]
'''
print('THE SECOND WAY')
lst.sort()
print(lst[0])
print(lst[-1])


'''
made by Gyanendra
'''
