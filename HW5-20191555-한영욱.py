#20191555-한영욱
#계산기 문제
##함수 선언

def add(x,y):
    return  x+y
def sub(x,y):
    return x-y
#몸체
print('계산기프로그램입니다. \n 1.덧셈 \n 2.뺄셈')

while True:
 실행=input('실행할 계산을 선택하여 주십시오.(1/2)')
 if 실행=='1' or 실행=='2':
     break
    
 print('올바른 수행코드를 입력하여주십시오.')
    


num1=int(input('첫번째 숫자를 입력하여주세요.'))
num2=int(input('두번째 숫자를 입력하여주세요.'))
if 실행=='1':
    print(num1,'+',num2,'+','=',add(num1,num2))
elif 실행=='2':
    print(num1,'+',num2,'-','=',sub(num1,num2))

   
