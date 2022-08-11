#HW5-퀴즈6-20191555-한영욱


#함수선언====================
def std_weight (x,y):
     if y=='여':
        return (x**2)*21
     elif y=='남':
        return (x**2)*22
   
 


#몸체===============

print('표준체중 제공 프로그램입니다')
x=int(input('키를 cm 단위로 입력하셔주십시오.'))
y=input('성별을 입력하여주십시오.(남/여)')
x=x/100
w=round(std_weight(x,y),2)
print('키 {}M의 {}자의 표준 체중은 {}입니다.'.format(x,y,w))
