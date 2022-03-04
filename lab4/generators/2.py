def IsEven(n):
    
    for i in range(n):
        if i%2==0:
            yield i
        i+=1


n=int(input())
ans = []

for i in IsEven(n):
    ans.append(str(i))

print (",".join(ans))
