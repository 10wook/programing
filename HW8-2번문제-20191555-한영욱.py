#HW8-2번 문제-20191555-한영욱
#함수를 사용하여 코딩하였고,
#친구추가, 친구삭제,친구 정보 수정의 경우 친구가 리스트에 존재하는지 확인하는 작업을 거쳤습니다.




#함수 선언========================================================================================
def find_friend(x):
    global f
    n=0
    for i in range(0,len(f)):
        if x==f[i][0]:
            n=n+1
    if n==1:
        return True
    else:
        return False
            
def del_friend(x):
    global f
    n=0
    for i in range(0,len(f)):
        if x==f[i][0]:
            n=f[i]
    f.remove(n)        
               
def cor_friend(x,y,z):
    global f
    n=0
    for i in range(0,len(f)):
        if x==f[i][0]:
            f[i]=(y,z)
           
                    
#몸체 선언=============================================================================================            
        

menu=0
f=[]
while menu!=9:
    print('===============친구 리스트 관리 프로그램입니다.===================')
    print('1.친구리스트 출력  \n 2.친구추가 \n 3.친구삭제 \n 4.정보수정 \n 9.종료')
    menu=int(input('메뉴를 선택하여 주십시오'))
    if menu==1:
        for name,phone in f:
            print(name)
            print(phone)
    elif menu==2:
        n=input('추가할 친구 이름을 입력해 주십시오.')
        if find_friend(n)==True:
            print('입력하신 친구는 이미 등록되어 있습니다.')
        else:
            num=input('입력하신 친구의 전화번호를 입력하여주십시오')
            profile=(n,num)
            f.append(profile)
            print('성공적으로 저장되었습니다.')
    elif menu==3:
        n=input('삭제할 친구 이름을 입력해주십시오')
        if find_friend(n)==True:
            del_friend(n)
            print('삭제되었습니다.')
        else:
            print('존재하지 않는 이름입니다.')
    elif menu==4:
        n=input('변경할 친구 이름을 입력해주십시오.')
        if find_friend(n)==True:
            nn=input('친구의 이름을 입력해주십시오.')
            nph=input('친구의 번호를 입력해주십시오.')
            cor_friend(n,nn,nph)
        else:
            print('올바른 이름을 입력하여주십시오.')
print('프로그램을 종료합니다.')            
            
            
