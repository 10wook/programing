#HW5-LAB1-3-20191555-한영욱


#함수선언======================
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def SQ(x,y):
    return x**y
def div2(x,y):
    return x//y,x%y
#몸체============================

while True:
    print('안녕하세요 계산기 프로그램입니다. \n 원하시는 계산을 선택하여주십시오.')
    print('프로그램종료:0 \n 덧셈:1 \n 뺄셈:2 \n 곱셈:3 \n 나눗셈:4 \n 제곱:5 \n 몫과 나머지 나눗셈:6')
    while True:
        실행=input('실행할 코드를 선택하여 주십시오.(0/1/2/3/4/5/6)')
        if 실행=='0' or 실행=='1' or 실행=='2' or 실행=='3' or 실행=='4'or 실행=='5' or 실행=='6':
            break
        print('올바른 코드를 입력하여주십시오.')

    if 실행=='0':
        print('프로그램을 종료합니다.')
        break

    else:   
     n1=int(input('첫번째 숫자를 입력하여주십시오.'))
     n2=int(input('두번쨰 숫자를 입력하여주십시오.'))

    if 실행=='1':
           print(n1,'+',n2,'=',add(n1,n2))
    elif 실행=='2':
            print(n1,'-',n2,'=',sub(n1,n2))
    elif 실행=='3':
            print(n1,'X',n2,'=',mul(n1,n2))
    elif 실행=='4':
            print(n1,'÷',n2,'=',div(n1,n2))
    elif 실행=='5':
        print(n1,'^',n2,'=',SQ(n1,n2))
    elif 실행== '6':

        a,b=div2(n1,n2)

        print(n1,'을', n2,'로 나누면 몫은',a,'이고, 나머지는',b,'입니다.')
            
           

