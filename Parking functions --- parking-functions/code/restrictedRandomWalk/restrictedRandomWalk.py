import random
import math
from pprint import pprint

def isResPF(pi, s):
    psi = sorted(pi)
    dyck = []
    c = len(pi)
    for i in range(c):
        dyck.append(i)
    for i in range(c):
        if psi[i] > dyck[i] or psi[i] > s or psi[i] < 0:
            return False
    return True

def isPF(pi):
    isResPF(pi, len(pi))

def randomStep(pi, s, cyclic):
    c = len(pi)
    if random.random() > 0.5:
        return pi
    j = random.randrange(c)
    if random.random() > 0.5:
        newpi = pi[0:j] + [pi[j] + 1] + pi[j + 1:]
        if isResPF(newpi, s):
            return newpi
        elif cyclic:
            newpi = pi[0:j] + [0] + pi[j + 1:]
            if isResPF(newpi, s):
                return newpi
        return pi
    else:
        newpi = pi[0:j] + [pi[j] - 1] + pi[j + 1:]
        if isResPF(newpi, s):
            return newpi
        elif cyclic:
            for i in range(s):
                newpi = pi[0:j] + [s - i] + pi[j + 1:]
                if isResPF(newpi, s):
                    return newpi
        return pi

def randomWalk(pi, s, cyclic):
    c = len(pi)
    for i in range(c**2):
            pi = randomStep(pi, s, cyclic)
    return pi

def lotsOfRandomWalks(pi, s, cyclic, N):
    piL = {}
    for i in range(N):
        newpi = tuple(randomWalk(pi, s, cyclic))
        if newpi in piL:
            value = piL[newpi]
            piL.update({newpi : value + 1})
        else:
            piL.update({newpi : 1})
    return piL

if __name__ == "__main__":
    pprint(lotsOfRandomWalks([0, 0, 0, 0, 0], 3 , True, 100000))
