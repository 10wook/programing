#HW14-LAB10-2-20191555-한영욱
def BubbleSort(x):
    for i in range(len(x)):
        n=i
        for j in range(0,len(x)-n-1):
            if x[j]>x[j+1]:
                x[j],x[j+1]=x[j+1],x[j]
l=[29,10,14,37,13,90]
print('Original List=%s'%l)
BubbleSort(l)
print("Sorted List by Bubble method")
print(l)
