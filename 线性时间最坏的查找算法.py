# -*- coding: utf-8 -*-
"""
Created on Mon May  8 19:26:07 2017

@author: Lenovo-Y430p
"""
#中位数排序的线性最优算法
def Partition(a, low,high, x):
    i=low
    high-=1
    while (a[i]!= x ) :
        i+=1 
    a[low],a[i]=a[i],a[low]
    while (low < high):
        while low < high and a[high] >= x:
            high-=1
        a[low] = a[high] 
        while low < high and a[low] <x:
            low+=1
        a[high] = a[low]
    a[low] = x
    return low 
def S_sort(a,low,high):
    n = high - low 
    if n==1:
        return a[low]
    remind=n%5                  
    for i in range(0,n//5):
        quick_sort(a, i*5+low,low+i * 5 + 4) 
        a[low+i],a[low+i * 5 + 2]=a[low+i * 5 + 2], a[low+i]
    h=n//5
    if remind !=0:
        quick_sort(a, high-remind,high-1)
        a[low+h],a[high-remind+(remind+1)//2-1]=a[high-remind+(remind+1)//2-1], a[low+h]
        x = S_sort(a, low,low+h+1)
    else: 
        x = S_sort(a, low,low+h)
    return x
def Select(a, low,high, k):  
    x=S_sort(a, low, high) 
    j= Partition(a, low, high, x)
    q = j - low + 1
    if (q == k) :
        return x
    elif (q>k): 
        return Select(a, low, j , k)
    else : 
        return Select(a, j+1, high, k - q)
def quick_sort(lists, left, right):
    # 快速排序
    if left >= right:
        return lists
    key = lists[left]
    least = left
    max1 = right
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    quick_sort(lists,least, left - 1)
    quick_sort(lists, left + 1, max1)
    return lists
a = [ 8, 4,0, -89, -12, 1, 36, 789, 21, 54,2,6,5,9,39,24,0]
t= Select(a, 0,len(a),10) 
print(t)