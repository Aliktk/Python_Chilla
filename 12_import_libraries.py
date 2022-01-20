# importing  module calc.py
import math
import statistics
print('value of pi is:' ,math.pi)


# importing sqrt() and factorial from the
# module math
from math import sqrt, factorial
  
# if we simply do "import math", then
# math.sqrt(16) and math.factorial()
# are required.
print(sqrt(16))
print(factorial(6))

# importing sys module
import sys
  
# importing sys.path
print(sys.path)

x = [10,20,80,6,100, 20]
print("means of x is :", statistics.mean(x))