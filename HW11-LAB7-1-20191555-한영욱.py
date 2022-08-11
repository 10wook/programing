#HW11-LAB7-1-20191555-한영욱
def 학생정보(이름,국어,수학,영어,과학):
    return {"이름":이름,"국어":국어,'수학':수학,'영어':영어,'과학':과학}
def 점수총합(x):
    return x['국어']+x['수학']+x['영어']+x['과학']
def 점수평균(x):
    return 점수총합(x)/4
학생들=[학생정보('윤인성',87,98,88,95),학생정보('연하진',92,98,96,98),학생정보('구지연',76,96,94,90),학생정보('나선주',98,92,96,92),학생정보('윤아린',95,98,98,98),학생정보('윤명월',64,88,92,92)]
print('==============딕셔너리로 성적 처리====================')
print('이름   총점    평균')
for i in 학생들:
    print('{}\t{}\t{}'.format(i['이름'],점수총합(i),점수평균(i)))



class Student:
    def __init__(self,name,korean,math,english,science):
        self.name=name
        self.korean=korean
        self.english=english
        self.math=math
        self.science=science


students = [
    Student('윤인성',87,98,88,95),
    Student('연하진',92,98,96,98),
    Student('구지연',76,96,94,90),
    Student('나선주',98,92,96,92),
    Student('윤아린',95,98,98,98),
    Student('윤명월',64,88,92,92)
]
print(students[0].math)
print('====================클래스기반 성적 처리========================')
print('이름   총점   평균')
for student in students:
    s=student.korean+student.math+student.english+student.science
    av=s/4

    print('{}\t{}\t{}'.format(student.name,s,av))
    
