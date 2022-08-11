#HW11-LAB8-1-20191555-한영욱
class Car:
    def __init__(self,speed):
        self.speed=speed
    def setspeed(self,speed):
        self.speed=speed
    def getDesc(self):
        return '차량=('+str(self.speed)+')'
class Sportcar(Car):
    def __init__(self,speed,turbo):
        super().__init__(speed)
        self.turbo=turbo
    def setturbo(self,turbo):
        self.turbo=turbo
print('(1)=============Car 클래스 상속에 의한 Sportcar 클래스 생성')
c=Sportcar(100,True)
print(c.getDesc())
c.setturbo(False)


