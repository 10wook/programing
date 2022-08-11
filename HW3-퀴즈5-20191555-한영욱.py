#HW3-퀴즈5-20191555-한영욱



from random import *
cnt=0
for i in range (1,51,1):
    time=randint(5,51)
    if time>=5 and time<=15:
        print('[0] {}번째 손님 (소요시간:{}분)'.format(i,time))
        cnt+=1
    else:
        print('[X] {}번째 손님 (소요시간:{}분)'.format(i,time))
print('총 탑승 승객 : {}분'.format(cnt))        
