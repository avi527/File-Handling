#program to open a file and print its attribute values
file=open("file1.txt","wb")
print("name of the file: ",file.name)
file.close()
print("file is closed.",file.closed)
print("file has been opened in",file.mode,'mode')

