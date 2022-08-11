#HW14-LAB10-3-20191555-한영욱
def InsertSort(x):
    for i in range(len(x)):
        standard=x[i]
        s=i-1
        while s>=0 and standard<x[s]:
            x[s+1]=x[s]
            s-=1
        x[s+1]=standard
            









l=[29,10,14,37,13,90]
print('original list=%s'%l)
InsertSort(l)
print('list Sorted by insert sort=%s'%l)
