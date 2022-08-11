#HW9-LAB5-1-20191555-한영욱
def f1(x):
    start,last=0,len(x)-1
    while True:
        if start>last:
            return True
        if x[start]!=x[last]:
            return False
        start+=1
        last-=1
def f2(x):
    for i in range(0,len(x)//2):
        if x[i]!=x[len(x)-1-i]:
            return False
    return True
def reverse(x):
    return x[::-1]
def f3(x):
    a=reverse(x)
    if a==x:
        return True
    else:
        return False

print('(1)===================================')
s=input('스트링을 입력해주십시오')
s=s.replace(" ","")
if f1(s)==True:
    print('{}는 회문입니다.'.format(s))
else:
    print('{}는 회문이 아닙니다.'.format(s))
print('(2)===================================')
s=input('스트링을 입력해주십시오')
s=s.replace(" ","")
if f2(s)==True:
    print('{}는 회문입니다.'.format(s))
else:
    print('{}는 회문이 아닙니다.'.format(s))
print('(3)===================================')
s=input('스트링을 입력해주십시오')
s=s.replace(" ","")
if f3(s)==True:
    print('{}는 회문입니다.'.format(s))
else:
    print('{}는 회문이 아닙니다.'.format(s))
