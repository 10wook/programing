#HW10-LAB6-2-20191555-한영욱
사전={ }
f="animal_eng.txt"
print('파일 전체를 출력합니다.')
with open (f,'r',encoding='utf-8') as file:
    print(file.read())
with open (f,'r',encoding='utf-8') as file:
    for line in file.readlines():
        x=line.split(',')
        사전[x[0]]=x[1].replace('\n','').replace(' ','')
    print('동물이름 영어사전을 출력합니다.')
    print(사전)
while 1:
    검색=input("동물의 한글 이름을 입력하여주십시오")
    답=검색.lower()
    if 답 in 사전:
        답=사전.get(답)
        print('{}는 영어로 {}입니다'.format(검색,답))
    else:
        print('등록되지 않은 이름입니다.')
