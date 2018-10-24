import copy
from fractions import Fraction, gcd

def answer(m):
	n = len(m[0])
	pprint(m)
	if sum(m[0])==0: 
		l = [1]
		for k in range(1,n): 
			if sum(m[k])==0: l.append(0)
		l.append(1)
		return l

	states = swap_rows(m)
	rows = isolate_q(m)
	m_fracs = to_frac(m)
	pprint(m)

	#define Q and R
	a = [[m_fracs[j][k] for k in range(0,rows)] for j in range(0,rows)]
	b = [[m_fracs[j][k] for k in range(rows,n)] for j in range(0,rows)]

	#I - Q
	subtract(a)

	res = gauss2(a,b)

	probs = res[0]
	dems = [k.denominator for k in probs]

	denom = lcmm(dems)

	ans = [denom/k.denominator * k.numerator for k in probs[0:len(probs)]]
	states = [k for k in states if k>0]
	order = [i[0] for i in sorted(enumerate(states), key= lambda x:x[1])]
	ans = [ans[o] for o in order]
	ans.append(denom)
	return ans

def swap_rows(m):
	rows = len(m)
	states = []
	for k in range(0,rows):
		if sum(m[k])==0: states.append(k)
		else: states.append(0)
	for k in range(0,rows):
		if sum(m[k])==0:
			for n in range(k+1,rows):
				if sum(m[n]) > 0:
					m[k],m[n] = m[n],m[k]
					states[k],states[n] = states[n], states[k]
					for j in range(0,rows): 
						m[j][k],m[j][n] = m[j][n],m[j][k]
					break
	return states

def isolate_q(m):
	size = len(m)
	for row in range(0,size):
		if sum(m[row])==0:
			mark = row
			break
	return mark

#ONLY RUN ON NONZERO ROWS!
def to_frac(m):
    a = copy.deepcopy(m)
    for row in range(0,len(a)):
    	denom = sum(a[row])
    	try:
        	a[row] = [Fraction(k,denom) for k in a[row]]
    	except ZeroDivisionError: pass
    return a

def subtract(q):
	siz = len(q)
	for k in range(0,siz):
		for z in range(0,siz):
			if k == z: q[k][z] = 1-q[k][z]
			else: q[k][z] = - q[k][z]


def gauss2(a, b):
    a = copy.deepcopy(a)
    b = copy.deepcopy(b)
    n = len(a)
    p = len(b[0])
    det = 1
    for i in range(n - 1):
        k = i
        for j in range(i + 1, n):
            if abs(a[j][i]) > abs(a[k][i]):
                k = j
        if k != i:
            a[i], a[k] = a[k], a[i]
            b[i], b[k] = b[k], b[i]
 
        for j in range(i + 1, n):
            t = a[j][i]/a[i][i]
            for k in range(i + 1, n):
                a[j][k] -= t*a[i][k]
            for k in range(p):
                b[j][k] -= t*b[i][k]
 
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            t = a[i][j]
            for k in range(p):
                b[i][k] -= t*b[j][k]
        t = 1/a[i][i]
        for j in range(p):
            b[i][j] *= t
    return b

def lcm(a, b):
    return a * b // gcd(a, b)

def lcmm(a): 
    return reduce(lcm, a)

def pprint(A):
    n = len(A)
    m = len(A[0])
    for i in range(0, n):
        line = ""
        for j in range(0, m):
            line += str(A[i][j]) + "\t"
        print(line)
    print("")

#mat = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

#mat = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

#mat = [[1, 0, 1, 0],[1, 0, 0, 0],[1,3,1,1],[0, 0, 0, 0]]

mat = [[1,0,1,0,0],[0,0,0,0,0],[0,1,0,0,0],[0,0,0,0,0],[3,1,0,3,4]]

print answer(mat)

