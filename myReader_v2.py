#!/usr/bin/python
fr = open('state.txt','r')
data = fr.readlines()

#print (data)
print('test')
print ("Your name:" + data[0])
line = input("Please enter the number of line to be modified:")
string = input("Please enter the content in that line: \n") 
# now change the 2nd line, note that you have to add a newline
x = int(line)-1
data[x] = string + "\n"
#! print out the line above and below
for i in range(0,3):
	print(data[x-1],end='')
	x = x+1
fr.close()

fw = open('state.txt','w')
fw.writelines(data)
fw.close()