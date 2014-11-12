import re

line = "Cats are smarter than dogs"

matchObj = re.match( r'(.*) are (.*?) .*', line, re.I)

if matchObj:
   print 1,  matchObj.group()
   print 2,  matchObj.group(1)
   print 3,  matchObj.group(2)
else:
   print "No match!!"
