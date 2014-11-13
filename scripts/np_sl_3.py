xm = np.array([[n+m*10 for n in range(5)] for m in range(5)])

xm[1:4, 1:4] # a block from the original array

xm[::2, ::2] # strides
