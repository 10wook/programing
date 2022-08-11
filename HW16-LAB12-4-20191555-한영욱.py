#HW16-LAB12-4-20191555-한영욱
#너무 어려워보이지만 나는 할 수 있다 ㄹㅇ 제발 하자
n=8

w=[]
from random import *
for i in range(0,8):
    w.append([])
    for j in range(0,8):
        if i==j:
            w[i].append(0)
        else:
            w[i].append(randint(1,30))

print('임의로 생성된리스트=%s'%w)
D=[[0]*(1<<n) for _ in range(n)]
total=(1<<n)-1
D2=[]






def find1(s,v):
    if v==total:
        return w[s][0] if w[s][0]>0 else 20202020
    if D[s][v]>0:
        return D[s][v]
    cost=20202020
    for i in range(1,n):
        if (v>>i)%2==1 or w[s][i]==20202020:continue

        tmp=find1(i,v|(1<<i))
        cost=min(tmp+w[s][i],cost)
    D[s][v]=cost
    return cost




def find2(w):
    li=[]
    from itertools import permutations
    l=list(permutations(range(1,n)))
    for i in l:
        a=w[0][i[0]]
        for j in range(0,n-2):
            a+=w[i[j]][i[j+1]]
        a=a+w[i[-1]][0]
        li.append(a)
    return min(li)
                
            
            
            
    
 
def find3(w):                            #find3 함수는 제가 처음에 구상했었던 코드입니다.  
        l=[]
        for a in range(1,n):             #이 코드는 n이 8일때만 작동하여 좋은 코드는 아니라고 생각합니다.
            for b in range(1,n):
                
                for c in range(1,n):
                   
                    for d in range(1,n):
                        
                        for e in range(1,n):
                   
                            for f in range(1,n):
                                if a==f or b==f or c==f or d==f or e==f:continue
                                for g in range(1,n):
                                    if a==b or a==g or b==g or c==g or d==g or e==g or f==g or a==c or b==c or a==d or b==d or c==d or a==e or b==e or c==e or d==e or a==f or b==f or c==f or d==f or e==f:continue
                                    l.append(w[0][a]+w[a][b]+w[b][c]+w[c][d]+w[d][e]+w[e][f]+w[f][g]+w[g][0])
        return  min(l)





import time as t
print('=========================================================')
btime=t.time()
a=find1(0,1)
atime=t.time()
print('12-3을 이용하여 구한 최단경로:%s'%a)
print('12-3을 이용한 최단경로 찾기에 걸린 시간:%s'%(atime-btime))


print('=========================================================')
btime=t.time()
a=find2(w)
atime=t.time()
print('동적 알고리즘을 이용하여 구한 최단경로:%s'%a)
print('동적 알고리즘을 이용한 최단경로 찾기에 걸린 시간:%s'%(atime-btime))


print('=========================================================')
btime=t.time()
a=find3(w)
atime=t.time()
print('초기에 생각했던 동적 알고리즘을 이용하여 구한 최단경로:%s'%a)
print('초기에 생각했던 동적 알고리즘을 이용한 최단경로 찾기에 걸린 시간:%s'%(atime-btime))
