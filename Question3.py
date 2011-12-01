def powerset(seq):
    """Return all the subsets of this set. This is a generator"""
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]]+item
            yield item

def testSubsetSum(l):
    """
    Find the number of all the subsets 
    where its max number equal to the sum of its remaining. 
    """
    n = 0
    for subset in powerset(l):
        if len(subset) <= 1:
            continue
        else:
            if subset[-1] ==  sum(subset[:-1]):
                print subset
                n += 1
    return n

if __name__ == '__main__':
    l = [3, 4, 9, 14, 15, 19, 28, 37, 47, 50, 54, 56, 59, 61, 70, 73, 78, 81, 92, 95, 97, 99]
    print testSubsetSum(l)
