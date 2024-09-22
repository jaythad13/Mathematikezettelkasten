def f(P): # outputs Q for given P
    p1 = P[0]
    p2 = P[1]
    p0 = P[2]
    Q = (p1*(p1**3 + 2*p2**3), - p2*(2*p1**3 + p2**3), p0*(p1**3 - p2**3))
    return Q
