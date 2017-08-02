#!/usr/bin/python

with open('state.txt','r') as file:
	#read a list of lines into data
	data = file.readlines()

print data
print "Your name:" + data[0]

# now change the 2nd line, note that you have to add a newline
data[1] = 'mage\n'

with open('state.txt','w') as file:
	file.writelines(data)
