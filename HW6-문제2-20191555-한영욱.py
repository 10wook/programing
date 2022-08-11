#HW6-2번 통합 문제-20191555-한영욱
#함수 선언=================
def is_prime(x):
    for i in range(2,x,1):
        if x%i==0:
           return False
           
    return True 

def find_prime(x,y):
    for i in range (x+1,y):
        is_prime(i)
        if is_prime(i)==True:
            return i

    return -1
def fn(x,y):
   a=1
   for i in range(2,x+1):
        if x%i==0 and y%i==0:
            a=i
   return a

def ufd(x,y):
    while y!=0:
        r=x%y
        x,y=y,r
    return x    

def c (상품값,n1000,n500,n100):
    C=(1000*n1000+500*n500+n100*100)-상품값
    c1000c=C//1000
    C=C%1000
    c500c=C//500
    C=C%500
    c100c=C//100
    C=C%100
    c50c=C//50
    C=C%50
    c10c=C//10
    C=C%10
    c1c=C/1
    return (c1000c,c500c,c100c,c50c,c10c,c1c)

def 평균():
    n=0
    합=0
    점수=0
    print('입력이 끝나면 -1 을 입력해주십시오.')
    while 점수>=0:
        점수=int(input('점수를 입력하여 주십시오.'))
        if 점수>0:
            합=합+점수
            n+=1
    if n>0:
        평균점수=합/n
    return 평균점수

#몸체=====================================================

while True:
    print('안녕하세요 복합 프로그램입니다. \n 원하시는 프로그램을 선택하여주십시오.')
    print('프로그램종료:0 \n 소수 확인 프로그램:1 \n 최대공약수 확인 프로그램:2 \n  거스름돈 계산 프로그램:3 \n 점수 평균 계산 프로그램:4 ')
    while True:
        실행=input('실행할 코드를 선택하여 주십시오.(0/1/2/3/4)')
        if 실행=='0' or 실행=='1' or 실행=='2' or 실행=='3' or 실행=='4':
            break
        print('올바른 코드를 입력하여주십시오.')

    if 실행=='0':
        print('프로그램을 종료합니다.')
        break
    elif 실행=='1':
        print('==============소수 찾기 프로그램입니다.====================')
        r=int(input('확인할 숫자를 입력하여주십시오,'))
        if is_prime(r)==True:
            print('입력하신',r,'은 소수입니다.')
        elif is_prime(r)==False:
            print('입력하신',r,'은 소수가 아닙니다.')
        print('두 수 사이의 소수중 가장 작은 소수를 찾으려고 합니다. 두 수를 입력하여 주십시오.')
        n1=int(input("두 수 중 작은 수를 입력하여 주십시오."))
        n2=int(input('두 수 중 큰 수를 입력하여 주십시오.'))
        r=find_prime(n1,n2)
        if r!= -1:
            print(n1,'과',n2,'사이의 가장 작은 소수 =',r)
        else:
            print('두 수 사이에 소수가 없습니다.')
        
    elif 실행=='2':
       print('===============최대 공약수를 찾아주는 프로그램입니다.=====================')
       n1=int(input('큰 수를 입력하여주십시오.'))
       n2=int(input('작은 수를 입력하여주십시오.'))
       print('일반 반복법으로 계산한',n1,'와',n2,' 사이의 최대 공약수',fn(n1,n2),'.')
       print('유클리드 방법으로 계산한',n1,'와',n2,' 사이의 최대 공약수',ufd(n1,n2),'.')
    elif 실행=='3':
        print("===========거스름돈 계산기입니다.================")
        i=int(input('물건 값을 입력하여 주십시오.'))
        n1000=int(input('천원짜리 지폐 지불 갯수를 입력하여주십시오,'))
        n500=int(input('오백원 짜리 동전 지불 갯수를 입력하여 주십시오'))
        n100=int(input('백원 짜리 동전 지불 갯수를 입력하여 주십시오'))
        a,b,c,d,e,f=c(i,n1000,n500,n100)
        print('1000원 짜리 지폐: {} \n 500짜리 동전 :{} \n 100원짜리 동전:{}\n 50원 짜리 동전 : {} \n 10원짜리 동전 : {} \n 1원짜리 동전 :{}'.format(a,b,c,d,e,f))
    elif 실행=='4':
         print('학생들의 점수를 입력하시면 평균을 알려드립니다.')
         print('평균=',평균())
         




       


