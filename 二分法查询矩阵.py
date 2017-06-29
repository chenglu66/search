# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 15:22:08 2017

@author: Lenovo-Y430p
"""
#二分法查询
def searchMatrix(matrix, target):
        #cost 866 ms
        # write your code here
        if len(matrix)==0:
            return False
        if target<matrix[0][0]:
            return False
        if target>matrix[-1][-1]:
            return False
        m=len(matrix);n=len(matrix[0])
        flag,index=getm(matrix,0,m,target)
        if flag:
            start=0
            end=n
            while 1:
                if start>=end:
                    print(1)
                    return False
                mid=(start+end)/2
                if target==matrix[index][mid]:
                    return True
                if target>matrix[index][mid]:
                    start=mid+1
                else:
                    end=mid
        else:
            return False
    #递归表达会慢一些
    '''
    def getm(self,matrix,start,end,target):
        if start>=end:
            return False,-1
        mid=(start+end)/2
        if target<=matrix[mid][-1] and target>=matrix[mid][0]:
            return True,mid
        elif target<matrix[mid][0]:
            return self.getm(matrix,start,mid,target)
        elif target>matrix[mid][-1]:
            return self.getm(matrix,mid+1,end,target)
    '''
def getm(matrix,start,end,target):
    while 1:
        if start>=end:
            return False,-1
        mid=(start+end)/2
        if target<=matrix[mid][-1] and target>=matrix[mid][0]:
            return True,mid
        elif target<matrix[mid][0]:
            end=mid
        elif target>matrix[mid][-1]:
            start=mid+1
def main():
    matrix=[7 [for i in range(7)] for j in range(7)]
    searchMatrix(matrix, 7)
if __name__=='__main__':
    main()