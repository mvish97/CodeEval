#To Pi or not to Pi
#get the input x add one to it and then add 1 to it and convert it to a string and return len-2
import math
from math import pi
file= open("sample.txt","r")
file1= file.readlines()
file2= []
for obj in file1:
    temp= obj.split()
    file2.append(temp[0])

"""for obj in file2:
    temp2 = "%." + obj + "f"
    final= temp2 % pi
    if(eval(obj) == 1):
        print(3)
    else:
        print(final[len(final)-2])"""


