'''Write a Python program that computes the net amount of a bank account based a
transaction log from console input. The transaction log format is shown as
following: D 100 W 200 (Withdrawal is not allowed if balance is going negative.
Write functions for withdraw and deposit) D means deposit while W means
withdrawal. Suppose the following input is supplied to the program:
D 300, D 300 , W 200, D 100 Then, the output should be: 500'''
class bankAcc:
    def _init_(self):
        self.balance=0
        print("Welcome to bank deposit nd withdrawal maChine")

    def deposit(self):
        amt=int(input("Enter amt to be deposited"))
        if amt>0:
            self.balance+=amt
            print("Amt deposited:",amt)
        else:
            print("Invalid amt")

    def withdraw(self):
        amt=int(input("Enter amt to be withdrawing"))
        if amt>0:
            if amt>=self.balance:
                self.balance=self.balance-amt
                print("Amt after withdrawing :",amt)
            else:
                print("insufficient balance")
        else:
            print("Invalid amt")

    def display(self):
        print("net bal :",self.balance)

s=bankAcc()
while True:
    print("1.Deposited")
    print("2.Withrawl")
    print("3.Display net balance")
    print("4. Exit")

    ch=int(input("Enter choice"))
    if ch==1:
        s.deposit()
    elif ch==2:
        s.withdraw()
    elif ch==3:
        s.display()
        break
    else:
        print("Exit")