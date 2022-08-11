#HW15-LAB11-2-20191555-한영욱
#퀵소팅
def partition(x,low,high):
    i=low-1
    standard=x[high]
    for j in range(low,high):
        if x[j]<standard:
            i=i+1
            x[i],x[j]=x[j],x[i]
    x[i+1],x[high]=x[high],x[i+1]
    return (i+1)




def QuickSort(x,low,high):
    if low<high:
        pi=partition(x,low,high)
        QuickSort(x,low,pi-1)
        QuickSort(x,pi+1,high)



a=[10,7,3,9,1,5]
print('original list=%s'%a)
n=len(a)
QuickSort(a,0,n-1)
print('Sorted list by QuickSort')
print(a)
