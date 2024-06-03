import random

def parkingSimulator(m, n, pref, front):
    "takes m cars, n spots, a preference matrix width a preference list for each car, and whether the car gets sent to the front or back. outputs the position of each car and the number of times each had to go around"
    tau = [-1]*n
    rev = [0]*m
    cars = []
    for i in range(m):
        cars.append(i)
    i = cars[0]
    while len(pref) > 0:
        i = cars[0]
        while len(pref[0]) > 0:
            p = pref[0][0]
            if tau[p] == -1:
                tau[p] = i
                pref.pop(0)
                cars.pop(0)
                break
            elif True:  #change to picky
                pref[0].pop(0)
                if (len(pref[0]) == 1) or (p < pref[0][1]):
                    ""
                else:
                    rev[i] += 1
                    if not front:
                        pref.append(pref.pop(0))
                        cars.append(cars.pop(0))
                        break
    return sum(rev)

def samplePreferenceMatrix(m, n, N):
    full_list1 = []
    full_list2 = []
    for i in range(N):
        M1 = []
        M2 = []
        for j in range(m):
            pi1 = samplePermutationList(n)
            pi2 = list(pi1)
            M1.append(pi1)
            M2.append(pi2)
        full_list1.append(M1)
        full_list2.append(M2)
    return full_list1, full_list2

def samplePermutationList(n):
    nums = []
    tau = []
    for i in range(n):
        nums.append(i)
    for i in range(n):
        j = random.randint(0, n - 1 - i)
        tau.append(nums.pop(j))
    return tau

def compareFrontBack(n, N):
    L1, L2 = samplePreferenceMatrix(n, n, N)
    revF = 0
    revB = 0
    for i in range(len(L1)):
        revF += parkingSimulator(n, n, L1[i], True)
    for i in range(len(L2)):
        revB += parkingSimulator(n, n, L2[i], False)
    return revF, revB
