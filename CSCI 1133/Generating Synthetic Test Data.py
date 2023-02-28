import random
fileobj = open('somefile','w')
##for i in range(2):
record = '' # start with a null string
for j in range(1,1001):
 record += str(j) + ',' # append each value and comma
 record += str(random.randint(-1000, 1000)) # strip off the last comma
 record += "\n"
fileobj.write(record)

fileobj.close()

