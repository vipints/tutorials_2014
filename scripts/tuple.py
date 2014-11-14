t = 12, 54, 'hello!'
print t[0]
#12

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print u
#((12, 54, 'hello!'), (1, 2, 3, 4, 5))

# Tuples are immutable:
t[0] = 88888

# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
print v
#([1, 2, 3], [3, 2, 1])
