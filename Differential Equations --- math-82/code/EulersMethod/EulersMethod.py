import math

def EulersMethod(x_0, t_0, t_f, h, xdot):
    x = [x_0]
    t = [t_0]
    xdots = []
    while (t[-1] < t_f):
        xdots.append(xdot(x[-1], t[-1]))
        x.append(xdots[-1] * h + x[-1])
        t.append(t[-1] + h)
    return x, xdots
