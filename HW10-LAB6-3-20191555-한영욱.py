#HW10-LAB6-3-20191555-한영욱
#학생1의 딕셔너리
김민수={'name':'김민수','assignment':[80,50,40,20],'test':[75,75],'lab':[67,90,78,72]}
#학생2의 딕셔너리
이민아={'name':'이민아','assignment':[82,56,44,30],'test':[83,95],'lab':[67,90,78,72]}
#학생3의 딕셔서닐
배철수={'name':'배철수','assignment':[77,82,23,39],'test':[75,78,77],'lab':[80,80]}
def 평균(x):
    합=sum(x)
    return 합/len(x)
def 개인성적(x):
    assignment=평균(x['assignment'])
    test=평균(x['test'])
    lab=평균(x['lab'])
    return (assignment*0.1+test*0.7+lab*0.2)
def abc성적(x):
    if x>=90:
        return "A"
    elif x>=80:
        return "B"
    elif x>=70:
        return "C"
    elif x>=60:
        return "D"
    else:
        return "F"

def 전체평균(x):
    전체=[]
    for i in x:
        개인=개인성적(i)
        전체.append(개인)
    return(평균(전체))
학생들=[김민수,이민아,배철수]
for i in 학생들:
    print(i['name'])
    print('============================')
    print('{}학생의 총점={}'.format(i['name'],개인성적(i)))
    print('{}학생의 성적={}'.format(i['name'],abc성적(개인성적(i))))
    print('============================')
          
반성적=전체평균(학생들)
print('반 전체 평균 점수=%0.2f'%(반성적))
print('반 전체 등급={}'.format(abc성적(반성적)))
