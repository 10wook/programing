#HW15-LAB11-1-20191555-한영욱
#머지소팅
def mergeSort(x):
    if len(x)>1:
        n=len(x)//2
        L=x[:n]
        R=x[n:]

        mergeSort(L)
        mergeSort(R)
        
        x.clear()
        while len(L)>0 and len(R)>0:
            if L[0]<=R[0]:
                x.append(L[0])
                L.pop(0)
            else:
                x.append(R[0])
                R.pop(0)

        for i in L:
            x.append(i)
        for i in R:
            x.append(i)
        


a=[10,7,3,9,1,5]
print('Original list=%s'%a)
mergeSort(a)
print('Sorted list by MergeSort')
print(a)

    
