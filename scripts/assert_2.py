
import sys

try:
    ph = sys.argv[1]
except:
    print 'Provide a phone number'

assert len(ph)==10, 'Not a valid Phone numnber %s' % ph 
