#! /usr/bin/env python
##!/usr/bin/python
########! /usr/bin/env python

def choose_pivot(iarray, lo, hi, method):
    if (method == 1):
        return lo 

def partion(iarray, lo, hi, pivot, nswap):
    pv = iarray[pivot]
    if (pivot != lo):
        iarray[lo],iarray[pivot] = iarray[pivot],iarray[lo]
        nswap += 1
    i = lo + 1 
    j = lo + 1
    while j < hi+1:
        if (iarray[j] < pv):
            if (j != i):
                iarray[i],iarray[j] = iarray[j],iarray[i]
                nswap += 1
            i += 1
        j += 1
    if (i-1) != lo :
        iarray[lo], iarray[i-1] = iarray[i-1], iarray[lo]
        nswap += 1
    return (i-1, nswap)
            


def myqsort(iarray, lo, hi, method, nswap):
    if (len(iarray) == 1):
        return nswap 
    else:
        p = choose_pivot(iarray, lo, hi, method)
        p, nswap = partion(iarray, lo, hi, p, nswap)
        if (p > lo):
            nswap = myqsort(iarray, lo, p-1, method, nswap)
        if (p < len(iarray)-1):
            nswap = myqsort(iarray, p+1, hi, method, nswap)
        return nswap


def main():
    with open('./array.txt', 'r') as f:
        iarray = map(int, f.readlines())
    print iarray
    nswap = myqsort(iarray, 0, len(iarray)-1, 1, 0)
    print iarray, nswap


if __name__ == "__main__":
    main()
