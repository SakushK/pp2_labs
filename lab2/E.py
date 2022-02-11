arr = []
n = input().split()

if(len(n)==2):
    x=int(n[1])
    n=int(n[0])
    
else:
    n=int(n[0])
    x=int(input())
  
  
for i in range(n):
    arr.append(x+2*i)

xor=0

for i in range(n):
    
    xor^=arr[i]
    
print(xor)
