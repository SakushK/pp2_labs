n=int(input())
exactly="@gmail.com"

ans=[]
string=""

for i in range(0,n):
    
    w=input()
    
    if exactly in w:
        
       c=w.strip(exactly)
       ans.append(c)
       
print('\n'.join(map(str,ans)))