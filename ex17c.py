from sys import argv 

script, from_file, to_file = argv

(indata, outdata) = (open(from_file).read()), (open(to_file, 'w'))
outdata.write(indata)

print "Alright, all done."

outdata.close()