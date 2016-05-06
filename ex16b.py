from sys import argv

script, filename = argv 

target = open(filename)
display = target.read() 

print "Here you go!\n%s " % display
 


