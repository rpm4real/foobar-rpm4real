def memorize(f):
    """ Memoization decorator for functions taking one or more arguments. """
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
def count_partitions2(n,m):
    # M IS ALWAYS ODD!!!!!!
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m <= 0:
        return 0
    else:
        return count_partitions2(n-m, m) + count_partitions2(n,m-2)
 
 
 
print (count_partitions2(192,191))