#HW7-퀴즈8-20191555-한영욱
class house:
    def __init__(self,위치,집종류,거래종류,가격,완공년도):
        self.위치=위치
        self.집종류=집종류
        self.거래종류=거래종류
        self.가격=가격
        self.완공년도=완공년도
    def show_detail(self):
       print(self.위치,self.집종류,self.거래종류,self.가격,self.완공년도)
houses=[]
house1=house('강남','아파트','매매','10억','2010년')
집2=house('마포','오피스텔','전세','5억','2007년')
집3=house('송파','빌라','월세','500/50','2000년')
       
houses.append(house1)
houses.append(집2)
houses.append(집3)
print('매물은 {}개 입니다.'.format(len(houses)))
for house in houses:
  house.show_detail()  
