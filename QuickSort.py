# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 18:23:05 2017

@author: cjrTaylor
"""

from random import randrange

def partition(alist, start, end, pivot):
    alist[pivot], alist[end] = alist[end], alist[pivot]
    temp_index = start
    for i in range(start, end):
        if alist[i] < alist[end]:
            alist[i], alist[temp_index] = alist[temp_index], alist[i]
            temp_index += 1
    alist[temp_index], alist[end] = alist[end], alist[temp_index]
    return temp_index

def quicksort(alist, start, end):
    if start >= end:
        return alist
    pivot = randrange(start, end + 1)
    new_pivot = partition(alist, start, end, pivot)
    quicksort(alist, start, new_pivot - 1)
    quicksort(alist, new_pivot + 1, end)

def sort(alist):
    quicksort(alist, 0, len(alist) - 1)
    return alist
