#! /usr/bin/env python
##!/usr/bin/python
########! /usr/bin/env python

def choose_pivot(iarray, lo, hi, method):
    if (method == 1):
        return lo 

def partion(iarray, lo, hi, pivot):
    pv = iarray[pivot]
    if (pivot != lo):
        iarray[lo],iarray[pivot] = iarray[pivot],iarray[lo]
    i = lo + 1 
    j = lo + 1
    while j < hi+1:
        if (iarray[j] < pv):
            if (j != i):
                iarray[i],iarray[j] = iarray[j],iarray[i]
            i += 1
        j += 1
    if (i-1) != lo :
        iarray[lo], iarray[i-1] = iarray[i-1], iarray[lo]
    return i-1
            


def myqsort(iarray, lo, hi, method, ncomp):
    if (lo == hi):
        return ncomp 
    else:
        ncomp = ncomp + (hi - lo)
        p = choose_pivot(iarray, lo, hi, method)
        p = partion(iarray, lo, hi, p)
        if (p > lo):
            ncomp = myqsort(iarray, lo, p-1, method, ncomp)
        if (p < hi-1):
            ncomp = myqsort(iarray, p+1, hi, method, ncomp)
        return ncomp


def main():
    with open('./array.txt', 'r') as f:
        iarray = map(int, f.readlines())
    iarray_ans = sorted(iarray)
    ncomp = myqsort(iarray, 0, len(iarray)-1, 1, 0)
    if iarray_ans == iarray:
        print ncomp
    else:
        print 'Wrong Answer'


if __name__ == "__main__":
    main()


