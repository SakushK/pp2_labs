import os
path=input()

print("Only directories:  ")
print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
print("Only files:  ")
print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])
print("All directories and files:  ")
print([ name for name in os.listdir(path)])
