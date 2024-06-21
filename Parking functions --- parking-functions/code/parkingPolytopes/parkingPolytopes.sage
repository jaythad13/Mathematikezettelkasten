def generateNonDecreasingPreferences(c, s):
	L = []
	for i in range(s**c):
		j = i
		pref = []
		for k in range(c):
			d = j % s
			pref.append(d)
			j = int(j / s)
		pref.sort()
		if pref not in L:
			L.append(pref)
	return L
