n=int(input())
a=[]

a = list(map(int,input().strip().split()))[:n]

a.sort()
   
    
print(a[-1]*a[-2])
