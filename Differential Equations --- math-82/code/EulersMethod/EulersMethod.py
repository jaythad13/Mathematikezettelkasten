import math

def EulersMethod(x_0, t_0, t_f, h, xdot):
    x = [x_0]
    t = [t_0]
    while (t[-1] < t_f):
        x.append(xdot(x[-1], t[-1]) * h + x[-1])
        t.append(t[-1] + h)
    return x

if __name__ == "__main__":
    print(EulerMethod(x_0, t_0, t_f, h, xdot))
