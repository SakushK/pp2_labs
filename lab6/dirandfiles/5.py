path = input()
list = input().split()

with open(path, 'w') as file:
        for x in list:
            file.write("%s\n" % x)
