# Python3 program for demonstration  
# of list index() method
  
list1 = [1, 2, 3, 4, 1, 1, 1, 4, 5]
  
# Will print the index of '4' in list1
print(list1.index(4))
  
list2 = ['cat', 'bat', 'mat', 'cat', 'pet']
  
# Will print the index of 'cat' in list2 
print(list2.index('cat'))


# Python3 program for demonstration 
# of index() method
  
list1 = [1, 2, 3, 4, 1, 1, 1, 4, 5]
  
# Will print index of '4' in sublist
# having index from 4 to 8.
print(list1.index(4, 4, 8))
  
# Will print index of '1' in sublist
# having index from 1 to 7.
print(list1.index(1, 1, 7))
  
list2 = ['cat', 'bat', 'mat', 'cat', 
         'get', 'cat', 'sat', 'pet']
  
# Will print index of 'cat' in sublist
# having index from 2 to 6
print(list2.index('cat', 2, 6 ))


# of index() method
  
list1 = [6 , 8 , 5 , 6 , 1 , 2]
  
# Will print index of '3' in sublist
# having index from 1 to end of the list.
print(list1.index(6 , 1))