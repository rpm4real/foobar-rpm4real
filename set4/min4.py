import random
from itertools import combinations

n = 5
base_set = range(0,n)
r = 2

#all_ntr = list(combinations(base_set,r))

#for ntr in all_ntr: 



exit()


all_possible = list(combinations(list(combinations(base_set,r)),n))
#print all_possible
found = False
for attempt in all_possible:
	if set.union(*[set(j) for j in attempt]) != set(base_set): 
		found = True
		break

if found: print "found", attempt
else: "failed"
