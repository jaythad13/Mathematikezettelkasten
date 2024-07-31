import math

def EulersMethod(x_0, t_0, t_f, h, xdot):
    x = [x_0]
    t = [t_0]
    xdots = []
    while (t[-1] < t_f):
        xdots.append(xdot(x[-1], t[-1]))
        x.append(xdots[-1] * h + x[-1])
        t.append(t[-1] + h)
    return x, xdots, t

def read(ar):
    l = len(ar[0]) - 1
    print("t \tx \tx'")
    for i in range(l):
        print(str(round(ar[2][i], 5)) + "\t" + str(round(ar[0][i], 5)) + "\t" + str(round(ar[1][i], 5)))
    print(str(round(ar[2][l], 5)) + "\t" + str(round(ar[0][l], 5)))

def ydot(y, t):
    return 1 - t + y # enter formula for y' here

if __name__ == "__main__":
    read(EulersMethod(1, 0, 1, 0.1, ydot)) # enter initial conditions here
