import math
from timeit import repeat

input = int(input('how many numbers of the fibonacci sequence do you want to see\n')) 


# 0 1 1 2 3 

a = 0
b = 1
c = 1

for x in range(0,input):
    c = b + a
    print(c)
    a = b
    b = c


    
   

