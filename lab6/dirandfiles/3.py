import os
path = input()

print('Exist:', os.access(path, os.F_OK))

if os.access(path, os.F_OK):
        print("All directories and files:  ")
        print([ name for name in os.listdir(path)]) 
else:
        print("[]")
