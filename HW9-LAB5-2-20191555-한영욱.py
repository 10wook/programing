#HW9-LAB-5-2-20191555-한영욱
def find_str(x,y):
    strs=x.split()
    a=[]
    for i in strs:
        if len(i)>y:
            a.append(i)
    return a

x=input('스트링 문자를 입력해주십시오')
y=int(input('숫자를 입력해주십시오'))

print(find_str(x,y))
