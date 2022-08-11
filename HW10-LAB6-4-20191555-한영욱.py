#HW10-LAB6-4-20191555-한영욱
f=input('파일 이름을 입력해주십시오')
print('파일 전체를 출력합니다.')
with open (f,'r',encoding='utf-8') as file:
    print(file.read())
print('(1)======================')
print('파일 내의 단어수 세기.')
with open(f,'r',encoding='utf=8') as file:
    for line in file .readlines():
        words=line.split()
        print('파일 내의 단어수=',len(words))
        

print('(2)======================')
def cntfile(x):
    with open (x,'r',encoding='utf-8')as infile:
        li=0
        for line in infile.readlines():
            L=line
            li+=len(L)
        return(li)

print('파일 내의 글자수={}'.format(cntfile(f)))
