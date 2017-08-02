#!/usr/bin/python
fr = open('state.txt','r')
data = fr.readlines()

print data
print "Your name:" + data[0]
line = raw_input("Please enter the number of line to be modified:")
string = raw_input("Please enter the content in that line: \n") 
# now change the 2nd line, note that you have to add a newline
data[int(line)] = string + "\n"
fr.close()

fw = open('state.txt','w')
fw.writelines(data)
fw.close()