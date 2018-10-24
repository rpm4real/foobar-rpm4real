from fractions import gcd

def answer(M,F):
	m = int(M)
	f = int(F)
	if m==1 and f==1: return 0
	result = euc(m,f)
	if result == 0: return "impossible"
	else: return result


def euc(a, b):
	iters = 0
	if a==1 or b==1: return abs(a-b)
	#print a,b
	while a>1 and b>1:
		mult = a/b
		a, b = b, a%b
		iters += mult
		#print a,b,"iters", iters
	if a==0 or b==0: return 0
	result = iters+abs(b-a)
	return result

def treed3(M,F):
	iters = 0
	while (M != 1 or F != 1):
		if M==F: return 0
		elif M>F: M = M-F
		else: F = F-M
		iters += 1	
		#print M,F
	return iters

a=19*18*17*16*15
b=1
print euc(a,b)
print treed3(a,b)






#prevs is a list of 2-lists which contain all options
def treed(prevs, goal, iters):
	#print "prevs=", prevs
	options = []
	for prev in prevs:
		options.append([prev[0]+prev[1],prev[1]])
		options.append([prev[0],prev[0]+prev[1]])
	prevs[:] = []
	#print "options=",options
	for o in options: 
		if o <= goal:
			prevs.append(o)
	iters[0] += 1
	#print iters[0]
	if goal in prevs: 
		#print iters[0]
		return 
	elif prevs == []: 
		iters[0]=0
		return 
	else:
		treed(prevs, goal, iters)

def treed2(M,F):
	pair = [M,F]
	iters = 0
	while (pair != [1,1]):
		if pair[0] == pair[1]: return 0
		pair[pair.index(max(pair))]=max(pair)-min(pair)
		iters += 1
	return iters



def treed4(M,F):
	if gcd(M,F) > 1: return 0
	else:
		iters = 0
		while (M != 1 or F != 1):
			if M>F: M = M-F
			else: F = F-M
			iters += 1
		print M,F
	return iters


#(100,500) was either (100,400) or (-400,500)

#(11,17) -> (11,6) -> (5,6) -> (5,1) (4,1) 3 2 1

