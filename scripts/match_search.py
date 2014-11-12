import re

line = "Cats are smarter than dogs";

matchObj = re.match( r'dogs', line, re.I)
if matchObj:
   print "match --> : ", matchObj.group()
else:
   print "No match!!"

searchObj = re.search( r'dogs', line, re.I)
if searchObj:
   print "search --> : ", searchObj.group()
else:
   print "Nothing found!!"
