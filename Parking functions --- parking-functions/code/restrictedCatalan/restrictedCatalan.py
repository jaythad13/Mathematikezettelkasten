import math

def Catalan(n):
    return math.comb(2*n, n)/(n + 1)

def restrictedCatalan(c, s):
    if s >= c:
        return Catalan(c)
    C = 0
    for i in range(1, s + 1):
        C = C + Catalan(i - 1) * restrictedCatalan(c - i, s - i + 1)
    return C

if __name__ == "__main__":
    N = int(input("How many Catalan triangle rows? \n"))
    for i in range(1, N):
        string = ""
        for j in range(1, i + 1):
            string = string + (f"({i}, {j}) = {restrictedCatalan(i, j)}\t")
        string = string + "\n"
        print(string)
