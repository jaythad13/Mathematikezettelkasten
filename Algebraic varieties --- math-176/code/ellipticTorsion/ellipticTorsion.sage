x = var('x')
f(x) = x^3 - 4*x + 4
x_infty = f(x).roots(x, ring=RR, multiplicities=False)[0]
Omega = integrate(1/sqrt(f(x)), x, x_infty, infinity)
x_0 = 2 
print(N(integrate(1/sqrt(f(x)), x, x_0, infinity)/(2*Omega)))

