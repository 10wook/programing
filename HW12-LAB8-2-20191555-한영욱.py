#HW11-LAB8-2-20191555-한영욱
class Person:
    def __init__(self,name,number):
        self.name=name
        self.number=number
class Student(Person):
    UNDERGRADUATE=0
    POSTGRADE=1
    def __init__(self,name,number,studenttype):
        super().__init__(name,number)
        self.studenttype=studenttype
        self.gpa=0
        self.classes=[]
    def enrollcourse (self,course):
        self.classes.append(course)
    def __str__(self):
        return '\n이름='+self.name+'\n주민번호='+self.number+'\n 수강과목='+str(self.classes)+'\n평점='+str(self.gpa)
class Teacher(Person):
    def __init__(self,name,number):
        super().__init__(name,number)
        self.courses=[]
        self.salary=30000000
    def assingteaching(self,course):
        self.courses.append(course)
    def __str__(self):
        return '\n이름='+self.name+'\n주민번호='+self.number+'\n 강의과목='+str(self.courses)+'\n월급='+str(self.salary)
print('(1)클래스 상속에 의한 학생, 선생님 클래스 생성=====')
홍=Student('홍길동','12345678',Student.UNDERGRADUATE)
홍.enrollcourse('자료구조')
print(홍)
김=Teacher('김철수','123456789')
김.assingteaching('파이썬')
print(김)
