d = 13 # non-square positive integer

def xp(z, n): # exponentiation
    if (n == 1):
        return z
    else:
        return mult(xp(z, n - 1), z)

def mult(z1, z2): # multiplication
    x1 = z1[0]
    y1 = z1[1]
    x2 = z2[0]
    y2 = z2[1]
    return(x1*x2 + d*y1*y2, x1*y2 + x2*y1)

def norm(z): # norm, for checking
    x = z[0]
    y = z[1]
    return(x**2 - d * y**2)
