#HW11-LAB7-2-20191555-한영욱
class Friend:
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
    def set_phone(self,phone):
        self.phone=phone
    def show_info(self):
        print('이름:',self.name)
        print('전화번호:',self.phone)
print('(1)===================클래스 기반의 연락처 관리========================')
f=Friend('한영욱','010-0000-0000')
f.set_phone('010-5555-5555')
f.show_info()
print('(2)===================클래스 기반의 연락처 관리========================')
#연락처를 리스트형태로 생성
frs=[]
frs.append(Friend('한영욱','0102222222'))
frs.append(Friend('강영욱','0102262222'))
frs.append(Friend('박영욱','0102282222'))
frs.append(Friend('김영욱','0102272222'))
for i in frs:
    i.show_info()
print('(3)===================클래스 기반의 연락처 관리========================')
for i in frs:
    if i.name.startswith('한'):
        i.show_info()

print('(4)===================클래스 기반의 연락처 관리========================')
for i in frs:
    if i.name=='김영욱':
        i.show_info()
