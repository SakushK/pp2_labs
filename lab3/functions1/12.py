def histogram( i ):
    for n in i:
        ans = ''
        times = n
        while( times > 0 ):
          ans += '*'
          times = times - 1
        print(ans)

l= [int(i) for i in input().split()]

histogram(l)
