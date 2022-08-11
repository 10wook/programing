#HW8-LAB4-1-20191555-한영욱


menu=0
f=[]
while menu!=9:
    print('===============친구 리스트 관리 프로그램입니다.===================')
    print('1.친구리스트 출력  \n 2.친구추가 \n 3.친구삭제 \n 4.이름변경 \n 9.종료')
    menu=int(input('메뉴를 선택하여 주십시오'))
    if menu==1:
        print(f)
        
    elif menu==2:
        n=input('추가할 친구 이름을 입력해 주십시오.')
        if n in f:
            print('입력하신 친구는 이미 등록되어 있습니다.')
        else:
            f.append(n)
    elif menu==3:
        n=input('삭제할 친구 이름을 입력해주십시오')
        f.remove(n)
    elif menu==4:
        n=input('변경할 친구 이름을 입력해주십시오.')
        if n in f:
            num=f.index(n)
            f[num]=input('새로운 이름을 입력해주십시오.')
        else:
            print('올바른 이름을 입력하여주십시오.')
print('프로그램을 종료합니다.')            
            
            
