fh = open("python_data.pickle", "rb")

xb = cPickle.load(fh)
fh.close() 

xa == xb # checking are they same #True 
