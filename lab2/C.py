n=int(input())

a = [[0]*n for i in range(n)]


for i in range(n):
      a[i][0]=i
      
for j in range(n):
        
        a[0][j]=j
        
for i in range(n):
    for j in range(n):
         if i==j:
            a[i][j]=i*j
            
for i in a:
        print(*i)
