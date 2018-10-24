import random
from itertools import combinations

elements = range(0,4)

n = 2

pairs = list(combinations(range(0,n),3))


sets = [set(i) for i in pairs]
'''
takes = list(combinations(range(0,n),3))
print takes
for take in takes:
	valid = False
	union = set.union(*[sets[t] for t in take])
	for j in elements:
		if j in union: pass
		else: 
			valid = True
			break
	if not valid: break 


if not valid: 
	print "Found r-1 union with all elements. Try Shifting"
	print take
	print union

if valid: print "good"
'''

all_possible = list(combinations(list(combinations(range(0,5),2)),5))
#print all_possible
found = False
for attempt in all_possible:
	if set.union(*[set(j) for j in attempt]) != set(range(0,5)): 
		found = True
		break

if found: print "found", attempt
else: "failed"
