#HW11-LAb8-3-20191555-한영욱
class Bankaccount:
    def __init__(self,name,number,balance):
        self.name=name
        self.number=number
        self.balance=balance
    def withdraw(self,amount):
        self.balance-=amount
        return self.balance
    def deposit (self,amount):
        self.balance+=amount
        return self.balance
#세이브 뱅크가 하는 일
#이자율 입력/이자 출력/이자 더하기
class Saveingaccount(Bankaccount):
    def __init__(self,name,number,balance,interest_rate):
        super(). __init__(name,number,balance)
        self.interest_rate=interest_rate
    def set_interest_rate(self,interest_rate):
        self.interest_rate=interest_rate
    def get_interest_rate(self):
        return self.interest_rate
    def add_interest_rate(self):
        self.balance+=self.balance*self.interest_rate

        


#체크카드가 하는일
#with draw 함수를 재정의하여 출금할때 수수료를 떼도록 만든다.
class Checkaccount(Bankaccount):
    def __init__(self,name,number,balance):
        super(). __init__(name,number,balance)
        
        self.withdraw_charge=10000
    def withdraw(self,amount):
        self.balance-=amount+self.withdraw_charge
        return self.balance








print('(1)======================은행계좌 클래스 및 클래스 상속==============')
a1=Saveingaccount('홍길동',123455,10000,0.05)
a1.add_interest_rate()
print(a1.balance)
a2=Checkaccount('김철수',1234566,2000000)
a2.withdraw(100000)
print(a2.balance)
