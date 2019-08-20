#program to write to a file using the writelines() method
file=open("avinash.txt","w")
lines=["hello world","welcome to the world of python","enjoy learning python"]
file.writelines(lines)
file.close()
print("data written in the file")
