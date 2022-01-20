x = 10
 
print("x is of type:",type(x))
 
y = 10.6
print("y is of type:",type(y))
 
x = x + y
 
print(x)
print("x is of type:",type(x))


# Python code to demonstrate Type conversion
# using int(), float()
 
# initializing string
s = "10010"
 
# printing string converting to int base 2
c = int(s,2)
print ("After converting to integer base 2 : ", end="")
print (c)
 
# printing string converting to float
e = float(s)
print ("After converting to float : ", end="")
print (e)