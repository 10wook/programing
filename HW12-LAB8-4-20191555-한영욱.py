#HW11-LAB8-4-20191555-한영욱
class Car:
    def __init__(self,speed,maker,model,color,price):
        self.speed=speed
        self.maker=maker
        self.model=model
        self.color=color
        self.price=price
    def setmaker(self,maker):
        self.maker=maker
    def setspeed(self,speed):
        self.speed=speed
    def getDesc(self):
        return '속도=('+str(self.speed)+') \n 메이커=('+str(self.maker)+') \n 모델=('+str(self.model)+') \n 색상=('+str(self.color)+') \n 가격=('+str(self.price)+')'
class Truck(Car):
    def __init__(self,speed,maker,model,color,price,payload):
        super().__init__(speed,maker,model,color,price)
        self.payload=payload
    def set_payload(self,payload):
        self.payload=payload
    def get_payload(self):
        return self.payload

class Bus(Car):
    def __init__(self,speed,maker,model,color,price,num_of_seats):
        super(). __init__(speed,maker,model,color,price)
        self.num_of_seats=num_of_seats
    def set_num_of_seats(self,num_of_seats):
        self.num_of_seats=num_of_seats
    def get_num_of_seats(self):
        return str(self.num_of_seats)
print('(1)=================클래스 기반 트럭 클래스 사용==============')
t=Truck(100,'벤츠','g클래스','회색',500000000,100)
print(t.getDesc())
print('트럭의 적재량'+str(t.get_payload())+'kg')
t.set_payload(200)
print('트럭의 적재량'+str(t.get_payload())+'kg')
print('(2)=================클래스 기반 버스  클래스 사용==============')
b=Bus(150,'현대','모델4','노란색',300000000,23)
print(b.getDesc())
print('버스의 탑승객'+str(b.get_num_of_seats())+'명')
b.set_num_of_seats(32)
print('버스의 탑승객'+str(b.get_num_of_seats())+'명')
