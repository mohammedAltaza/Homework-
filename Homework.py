#Question 1: Python Basics? 

#A
L1 = ['HTTP', 'HTTPS','FTP', 'DNS']
L2=[80,443,21,53]
d= {}
for i in range(len(L1)):
 d.__setitem__(L1[i], L2[i])
print(d)

#B
number = int(input("Enter number :"))
n = 1
for i in range(1, number + 1):
    n *= i
print(n)

#C
L=['Network' , 'Bio' , 'Programming', 'Physics' , 'Music']
for i in range(len(L)) :
 if L[i].startswith("B"):
  print(L[i] , ':' , L[i][0:1]," ///////////", 'The Right one' )

#D                                                                              
d={x:x+1 for x in range(11)}
print(d)

#===========================================================
#Question 2: Convert from Binary to Decimal

Binary=input('enter your number :') 
try:
    x= int(Binary,2)
    print(x)
except: 
  print('enter your correct number')

#==========================================================
#Question 3: Working with Files” Quiz Program”

import json
f=open('E:\medoo.json','r')
test = json.load(f)
f.close()
name=input("enter name:")
number=input("enter number:")
grad=0
for i in test:
  ans = int (input (i))
  if ans == test[i]:
      grad = grad + 1 
d=open('E:\ mohammad.json','w')
json.dump ({"name" : name , "number" : number , "grad" : grad},d)

#========================================================
#Question 4: Object-Oriented Programming - Bank Class

class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0 

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount  # إضافة المبلغ إلى الرصيد

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount  # خصم المبلغ من الرصيد

    def get_balance(self):
        return self.balance  # إعادة الرصيد الحالي
    
    # إنشاء كائن من الصنف BankAccount
account = BankAccount("Mm1212", "Mohammad Altaza")
# إجراء الإيداع
account.deposit(1000)
print("Current balance after deposit :", account.get_balance())
# إجراء السحب
account.withdraw(500)
print("Current balance after withdrawal :", account.get_balance())
class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate):
        super().__init__(account_number, account_holder)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.deposit(interest)  # تطبيق الفائدة على الرصيد

    def __str__(self):
       return f"account number : {self.account_number},  Account owner : {self.account_holder},Balance: {self.balance},interest rate : {self.interest_rate}%"
    
# إنشاء كائن من SavingsAccount
savings_account = SavingsAccount("Mm09988", " Mohammad", 5)

# إجراء الإيداع
savings_account.deposit(1000)

# تطبيق الفائدة
savings_account.apply_interest()

# طباعة تفاصيل الحساب بعد تطبيق الفائدة
print(savings_account)

#========================================================