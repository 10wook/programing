#HW14-LAB10-1-20191555-한영욱

##    sort1은 교수님이 수업중에 알려주신 Selection Sorting 방법입니다.
##    sort0는 제가 이해한 방식으로 Selection Sorting을 구현한 방법인데
##    어떤 차이가 있는 것인지 궁금합니다

l=[64,25,12,22,11]

def sort1(x):                   #이 부분이 교수님이 수업중에 알려주신 코드였습니다.
    for i in range(len(x)):
        min=i
        for j in range(i+1,len(x)):
            if x[min]>x[j]:
                min=j
        x[i],x[min]=x[min],x[i]
    return x


j=[64,25,12,22,11]
def sort0(x):                 #이 부분은 제가 교수님의 설명을 듣고만든 sort코드입니다.
    for i in range(len(x),0,-1):
          newlist=x[0:i]
          M=max(newlist)
          r=newlist[i-1]
          switchplace=x.index(M)
          x[i-1],x[switchplace]=x[switchplace],x[i-1]
    return x

print('original list=%s'%l)
sort1(l)
print('Sorted list by Selection method')
print(l)



print('===========================================')
print('original list=%s'%j)
sort0(j)
print('Sorted list by Selection method')
print(j)
#제가 만든 방법으로 하면 안되는 건가요???
