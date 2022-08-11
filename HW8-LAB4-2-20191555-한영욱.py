#HW8=LAB4-2-20191555-한영욱
list1=[6,5,4,1,2,3]
print('=========================두번째 큰수 찾기 프로그램================')
print('원래 리스트는 {}입니다.'.format(list1))
mx=max(list1[0],list1[1])
smx=min(list1[0],list1[1])
n=len(list1)
for i in range(2,n):
    if list1[i]>mx:
        smx=mx
        mx=list1[i]
    elif list1!=mx and list1[i]>smx:
        smx=list1[i]
    else:
        if smx==mx:
            smx=list[i]
print('두번째로 큰수는 {}입니다.'.format(smx))
print('=========================두번째 큰수 찾기 프로그램================')
print('원래 리스트는 {}입니다.'.format(list1))
list1.sort()
print('두번째로 큰수는 {}입니다.'.format(list1[-2]))
print('=========================두번째 큰수 찾기 프로그램================')
list1=[6,5,4,1,2,3]
print('원래 리스트는 {}입니다.'.format(list1))
nlist=set(list1)
nlist.remove(max(nlist))
print('두번째로 큰수는 {}입니다.'.format(max(nlist)))
