

files = open('basics/drek.txt')
#print(files.read())
#print(files.readline())
#print(files.readline())



#for line in files.readlines():
   # print(line)

#line = files.readline()

#while line != "":
 #   print(line)
 #   line = files.readline()

#files.close()

with open('basics/drek.txt') as reader:
    content = reader.readlines()
    rev = reversed(content)
    with open('basics/drek.txt', 'w') as writer:
        for line in rev:
            writer.write(line)






