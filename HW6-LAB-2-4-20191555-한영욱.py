#HW6-LAB-2-4-20191555-한영욱
#학생들 평균 구하기 프로그램
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
print('학생들의 점수를 입력하시면 평균을 알려드립니다.')
print('평균=',평균())
