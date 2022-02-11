d = [int(i) for i in input().split()]

way=[False for i in d[1:]]

way.append(True)

for i in range(len(d)-2,-1,-1):
    if d[i]>=way.index(True)-i:
       way[i]=True

if way[0]:
    print(1)
else:
    print(0)
