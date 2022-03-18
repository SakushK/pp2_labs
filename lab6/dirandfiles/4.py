path = input()
file = open(path, 'r')
content = file.read()
lines = content.split('\n')

print (str(len(lines))+" lines")
