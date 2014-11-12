def compute_factorial(n):
    """
    computes factorial of n
    """

    ret = 1
    for i in xrange(n):
        ret=ret*(i+1)

    return ret
