# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 18:37:45 2017

@author: cjrtaylor
"""

def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        leftHalf = alist[:mid]
        rightHalf = alist[mid:]
        
        mergeSort(leftHalf)
        mergeSort(rightHalf)
        
        i=0
        j=0
        k=0
        
        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[i]:
                alist[k]=leftHalf[i]
                i+=1
            else:
                alist[k]=rightHalf[j]
                j+=1
            k+=1
        
        while i < len(leftHalf):
            alist[k]=leftHalf[i]
            i+=1
            k+=1
        
        while j < len(rightHalf):
            alist[k]=rightHalf[j]
            j+=1
            k+=1
