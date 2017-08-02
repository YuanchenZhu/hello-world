#!/usr/bin/python
fr = open('state.txt','r')
data = fr.readlines()

print data
print "Your name:" + data[0]

# now change the 2nd line, note that you have to add a newline
data[1] = 'mage\n'
fr.close()

fw = open('state.txt','w')
fw.writelines(data)
fw.close()