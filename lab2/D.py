n = int(input()) 
 
a = [['.']*n for i in range(n)] 

if n%2!=0: 
    for i in range(n): 
        for j in range(n): 
            if i+j>=n-1: 
                a[i][j] = "#" 
 
 
if n%2==0: 
    for i in range(n): 
        for j in range(n): 
            if i>=j: 
                a[i][j] = "#" 
  
 
for i in a: 
    print(''.join(str(x) for x in i))
                
