#calling close() on a file object that is already closed does not raise any error
#but fails sileently as show below

with open("sudher.txt","r") as file:
    print(file.read())
file.close()
