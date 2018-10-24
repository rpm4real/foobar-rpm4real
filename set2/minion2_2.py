def answer(l):
	if(len(l)==0): 
		return 0
	if sum(l) % 3 == 0: return quick_int(l)
	win=0
	for k in l: 
		check = list(l)
		check.remove(k)
		if (sum(check) % 3==0 and len(check)>0): 
			tot = quick_int(check)
			if tot > win: 
				win = tot
	#base case
	if win>0:
		return win
	#recursive step
	else:
		winj = 0
		for j in l:
			dropj = list(l)
			dropj.remove(j)
			checkj = answer(dropj)
			if checkj > winj: winj = checkj
		return winj

def quick_int(l):
	return int(''.join(str(k) for k in sorted(l)[::-1]))

