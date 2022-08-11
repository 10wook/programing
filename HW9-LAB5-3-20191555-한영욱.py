#HW9-LAB5-3-20191555-한영욱
jm=input('주민번호를 000000-000000형태로 입력하여 주십시오')
y=int(jm[0:2])
m=int(jm[2:4])
d=int(jm[4:6])
if jm[7]=='3' or jm[7]=='4':
    a=2000+y
    print('당신은 {}년생 이고 {}월{}일에 태어났군요'.format(a,m,d))
    
else :
    a=1900+y
    print('당신은 {}년생이고 {}월{}일에 태어났군요'.format(a,m,d,))
    
if jm[7]=='3' or jm[7]=='1':
    print('또한 당신의 성별은 남성이군요.')
else:
    print('또한 당신의 성별은 여성이군요')
print('그리고 나이는 {}살이군요'.format(2021-int(a)))
