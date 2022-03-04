def IsThreeFour(n):
    
    for i in range(n):
        if i%3==0 and i%4==0:
            yield i
        i+=1


n=int(input())
ans = []

for i in IsThreeFour(n):
    ans.append(i)

print (ans)
