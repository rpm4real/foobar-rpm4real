from string import printable

def answer(n,b):
	length = len(n)
	#initialize list of results
	diffs = [int(n)]

	while ( not_twice(diffs) ):
		x = list(n)
		#turn to list of ints
		x = [int(k) for k in x]

		sort = sorted(x)
		aesc = ''.join(str(k) for k in sort)
		desc = ''.join(str(k) for k in aesc[::-1])

		result = from_base10(int(desc,b) - int(aesc,b),b)
		result = int2pad(str(result),length)
		diffs.append(result)
		n = result
		print desc, '-', aesc, '=', n

	pos = diffs.index(diffs.pop())
	return len(diffs)-pos

def not_twice(a):
	if a.count(a[-1]) > 1 :
		return False
	else:
		return True

def int2pad(string,length):
	stringl = list(string)
	while (len(stringl) != length):
		stringl.insert(0,'0')
	return ''.join(stringl)

def from_base10(x,b):
	res = ''
	while x > 0:
		res = printable[x % b] + res
		x //= b
	return res



print answer('11754',8)


