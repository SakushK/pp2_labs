def all(n):
    i=n 
    
    while(i!=-1):
        
        yield i
        i-=1
        
n=int(input())

for i in all(n):
    
    print(i,end=" ")
