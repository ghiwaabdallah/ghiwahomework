#Question 1 -A

list1=['HTTP','HTTPS','FTP','DNS']
list2=[80,443,21,53]
l={l1:l2 for (l1,l2)in zip(list1,list2)}
print(l)



#Question 1 -B

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter a number: "))
result = factorial(num)
print(f"The factorial of {num} is {result}")



#Question 1 -C

L = ['Network', 'Bio', 'Programming', 'Physics', 'Music']

for item in L:
    if item.startswith('B'):
        print(item)



#Question 1 -D

d = {i: i+1 for i in range(11)}
print(d)


#Question 2

# Read the binary number from the user
binary_number = input("Enter a binary number: ")

# Convert the binary number to decimal
decimal_number = 0
for digit in binary_number:
    decimal_number = decimal_number*2 + int(digit)

# Display the equivalent decimal number
print(f"The equivalent decimal number is: {decimal_number}")



#Question 3

a=open("D:\Ghiwa.txt","r")
b=a.read()
c=b.splitlines()
u=[]
v=[]
for i in range(0,40,2):
    u.append(c[i])
for i in range (1,40,2):
    v.append(c[i])

score=0
name=input("enter your name: ")
for i in range(len(u)):
    print(u[i])
    an=input("the answer: ")
    if an==v[i]:
        score+=1
    else:
        print("false")
print(name,":" ,score)
x=open("D:\Gh.txt","w")
y=[name,str(score)]
x.writelines(y)
a.close()
x.close()




#Question 4

class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. Current balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Current balance: ${self.balance}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0.0, interest_rate=0.02):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest

    def print(self):
        print(f"Current balance: ${self.balance}, Interest rate: {self.interest_rate * 100}%")


bank_acc = BankAccount("12345", "ghiwa abd")
bank_acc.deposit(1000)
bank_acc.withdraw(500)
print(f"Final balance: ${bank_acc.get_balance()}")

# Create an instance of SavingsAccount
savings_acc = SavingsAccount("54321", "gazal abd", 2000, 0.05)
savings_acc.apply_interest()
savings_acc.print()
