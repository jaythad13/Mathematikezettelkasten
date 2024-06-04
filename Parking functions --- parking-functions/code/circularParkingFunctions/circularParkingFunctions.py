import random
import numpy as np

def parkingSimulator(m, n, pref, front, picky):
    "takes m cars, n spots, a preference matrix with a preference list for each car, and whether the car gets sent to the front or back. outputs the position of each car and the number of times each had to go around"
    tau = [-1]*n
    rev = [0]*m
    cars = []
    for i in range(m):
        cars.append(i)
    i = cars[0]
    while len(cars) > 0:
        i = cars[0]
        while len(pref[0]) > 0:
            p = pref[0].pop(0)
            if p == -1:
                cars.pop(0)
                pref.pop(0)
                break
            if tau[p] == -1:
                tau[p] = i
                pref.pop(0)
                cars.pop(0)
                break
            elif len(pref[0]) < 1: #only happens if picky
                for i in range(n - 1):
                    pref[0].append((p + i)%n)
                    pref[0].append(-1)
            if (p < pref[0][0]):
                ""
            else:
                rev[i] += 1
                if not front:
                    pref.append(pref.pop(0))
                    cars.append(cars.pop(0))
                    break
    return rev, tau

def samplePreferenceMatrix(m, n, ofthem, N):
    full_list1 = []
    full_list2 = []
    for i in range(N):
        M1 = []
        M2 = []
        for j in range(m):
            pi1 = samplePermutationList(n, ofthem)
            pi2 = list(pi1)
            M1.append(pi1)
            M2.append(pi2)
        full_list1.append(M1)
        full_list2.append(M2)
    return full_list1, full_list2

def samplePermutationList(n, ofthem):
    nums = []
    tau = []
    for i in range(n):
        nums.append(i)
    for i in range(ofthem):
        j = random.randint(0, n - 1 - i)
        tau.append(nums.pop(j))
    return tau

def compareFrontBackPicky(n, N):
    L1, L2 = samplePreferenceMatrix(n, n, n, N)
    revF = [0]*n
    revB = [0]*n
    for i in range(len(L1)):
        addToRevF = parkingSimulator(n, n, L1[i], True, True)
        for j in range(n):
            revF[j] += addToRevF[j]
    for i in range(len(L2)):
        addToRevB = parkingSimulator(n, n, L2[i], False, True)
        for j in range(n):
            revB[j] += addToRevB[j]
    return (revF, revB)

def compareFrontBackNotPicky(n, ofthem, N):
    L1, L2 = samplePreferenceMatrix(n, n, ofthem, N)
    revF = [0]*n
    revB = [0]*n
    for i in range(len(L1)):
        addToRevF = parkingSimulator(n, n, L1[i], True, False)[0]
        for j in range(n):
            revF[j] += addToRevF[j]
    for i in range(len(L2)):
        addToRevB = parkingSimulator(n, n, L2[i], False, False)[0]
        for j in range(n):
            revB[j] += addToRevB[j]
    return (revF, revB)

def countPermutations(n, ofthem, N):
    L1, L2 = samplePreferenceMatrix(n, n, ofthem, N)
    print(L1)
    frontPerm = {}
    backPerm = {}
    for i in range(len(L1)):
        tau = tuple(parkingSimulator(n, n, L1[i], True, True)[1])
        if tau in frontPerm:
            frontPerm.update({tau : frontPerm[tau] + 1})
        else:
            frontPerm.update({tau : 1})
    for i in range(len(L2)):
        tau = tuple(parkingSimulator(n, n, L2[i], False, True)[1])
        if tau in backPerm:
            backPerm.update({tau : backPerm[tau] + 1})
        else:
            backPerm.update({tau : 1})
    return frontPerm, backPerm

if __name__ == "__main__":
    frontPerm, backPerm = countPermutations(3, 3, 1)
    print (frontPerm, backPerm)
