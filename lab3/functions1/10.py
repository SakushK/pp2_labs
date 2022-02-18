def unique_list(l):

    new = []

    for i in l:

        if i not in new:

            new.append(i)

    return new

s= [int(i) for i in input().split()]

print(unique_list(s))
