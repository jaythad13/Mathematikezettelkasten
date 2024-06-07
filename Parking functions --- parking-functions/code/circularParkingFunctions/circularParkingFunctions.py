import random
import numpy as np
import copy

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
            #if p == -1:
                #cars.pop(0)
                #pref.pop(0)
                #break
            if tau[p] == -1:
                tau[p] = i
                pref.pop(0)
                cars.pop(0)
                break
            elif len(pref[0]) < 1: #only happens if not picky
                for j in range(1, n):
                    pref[0].append((p + j)%n)
                    #pref[0].append(-1)
            if (p < pref[0][0]):
                ""
            else:
                rev[i] += 1
                if not front:
                    pref.append(pref.pop(0))
                    cars.append(cars.pop(0))
                    break
    return tau

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

def compareFrontBackPicky(m, n, N):
    L1, L2 = samplePreferenceMatrix(m, n, n, N)
    revF = [0]*n
    revB = [0]*n
    for i in range(len(L1)):
        addToRevF = parkingSimulator(m, m, L1[i], True, True)
        for j in range(n):
            revF[j] += addToRevF[j]
    for i in range(len(L2)):
        addToRevB = parkingSimulator(m, m, L2[i], False, True)
        for j in range(n):
            revB[j] += addToRevB[j]
    return (revF, revB)

def compareFrontBackNotPicky(m, n, ofthem, N):
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

def countPermutations(m, n, ofthem, N):
    L1, L2 = samplePreferenceMatrix(m, n, ofthem, N)
    print(L1)
    frontPerm = {}
    backPerm = {}
    for i in range(len(L1)):
        tau = tuple(parkingSimulator(m, m, L1[i], True, True)[1])
        if tau in frontPerm:
            frontPerm.update({tau : frontPerm[tau] + 1})
        else:
            frontPerm.update({tau : 1})
    for i in range(len(L2)):
        tau = tuple(parkingSimulator(m, m, L2[i], False, True)[1])
        if tau in backPerm:
            backPerm.update({tau : backPerm[tau] + 1})
        else:
            backPerm.update({tau : 1})
    return frontPerm, backPerm

def generatePreferences(c, s): #note, pref of car 1 will always be spot 0
    L = []
    for i in range(s**(c - 1)):
        j = i
        pref1 = [[0]]
        pref2 = [[0]]
        for k in range(c - 1):
            d = j % s 
            pref1.append([d])
            pref2.append([d])
            j = int(j / s)
        L.append((pref1, pref2))
    return L

def checkBinomialBijection(n):
    L = generatePreferences(n, n + 1)
    k1tok2 = {}
    for pair in L:
        pref1 = pair[0]
        pref2 = pair[1]
        k1 = numNs(pref2, 0)
        tau = parkingSimulator(n, n + 1, pref1, True, False)
        hole = tau.index(-1)
        shift = (n + 1 - hole) % (n + 1)
        new0 = (n + 2 - shift) % (n + 1)
        k2 = numNs(pref2, new0)
        if (k1, k2) in k1tok2:
            k1tok2.update({(k1, k2) : (k1tok2[(k1, k2)] + 1)})
        else:
            k1tok2.update({(k1, k2) : 1})
    return k1tok2

def numNs(L, N):
    count = 0
    for i in range(len(L)):
        if L[i][0] == N:
            count += 1
    return count

if __name__ == "__main__":
    N = 9
    for n in range(1, N):
     L = checkBinomialBijection(n)
     print(L)
     for key in L.keys():
         if L[key] != L[(key[1], key[0])]:
                 print(False)

    # i_ones = [0]*(n + 1)
    #for i in range(n + 1):
     #   for k in L.keys():
      #      if k[0] == i:
       #         i_ones[i] += L[k]/(n + 1)
