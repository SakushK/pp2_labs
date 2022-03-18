from time import sleep
import math 
n = int(input("Sample Input:"))

t = int(input())
sleep(t/1000)

print("Sample Output:")
print("Square root of " + str(n) +  " after "+ str(t)+" miliseconds is "+ str(math.sqrt(n)))
