import sys 
import cPickle 

xa = ['mango', 'carrots', 'garlic']

fh = open("python_data.pickle", "wb")

cPickle.dump(xa, fh, protocol=2) 
fh.close() 
