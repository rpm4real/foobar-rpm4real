def answer(n):
	if n % 2 == 1: m = n
	else: m = n-1

	return count_partitions(n,m)


def memorize(f):
    class memodict(dict):
        def __init__(self, f):
            self.f = f
        def __call__(self, *args):
            return self[args]
        def __missing__(self, key):
            ret = self[key] = self.f(*key)
            return ret
    return memodict(f)


@memorize 
def count_partitions(n,m):
    # M IS ALWAYS ODD!!!!!!
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m <= 0:
        return 0
    else:
        return count_partitions(n-m, m) + count_partitions(n,m-2)


print answer(192)