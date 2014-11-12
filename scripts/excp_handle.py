
try:
   fh = open("testfile", "r") # reading the file 
except IOError:
   print "Error: can\'t find file for reading"
