''' Examples - Quadratic Complexity '''


# example1
def is_subset(L1, L2):
    ''' determine if one list is subset of second(assume no duplicates) '''
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True


# example2
def intersect(L1, L2):
    ''' find intersection of two lists, return a list with each element
    appearing only once '''
    tmp = []
    for e1 in L1:
        for e2 in L2:
            if e1 == e2:
                tmp.append(e1)
    res = []
    for e in tmp:
        if not(e in res):
            res.append(e)
    return res
