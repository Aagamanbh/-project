class Bankaccount():

    def __init__(self,name,phone,balance=0.00):
        self.name=name
        self.phone=phone
        self.balance=balance

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"Account is deposited by  Rs.{amount},Balance after deposit is Rs.{self.balance} ")
        else:
            print(f"Enter amount greater than zero.")

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print( f"You account is withdrawn by Rs.{amount},balance after withdraw is Rs.{self.balance}")
        else:
            print(f"You have insufficient amount.")

    def details(self):
        print(f"Name:{self.name} ; Phone:{self.phone} ; balance={self.balance}")
# s1=Bankaccount("Aagaman","9389398390",50000)
# s1.details()
# s1.deposit(2000)
# s1.withdraw(5000)
# s1.withdraw(49000)
def miniatm():
    print("Welcome to Mini-ATM")
    name=input("Enter your name:  ")
    phone=input("Enter you phone: ")
    balance=int(input("Enter your amount to save: "))
    account=Bankaccount(name,phone,balance)

    while True:

        choice=input("""
                 1.Check Balance
                 2.Deposit
                 3.Withdraw
                 4.Exit   
                 Choose the following(1-4): """)
        if(choice=="1"):
            account.details()
        elif(choice=="2"):
            amount=int(input("Enter the amount to deposit: "))
            account.deposit(amount)
        elif(choice=="3"):
            amount=int(input("Enter the amount to withdraw: "))
            account.withdraw(amount)
        elif(choice=="4"):
            print("Thank-you for using Mini-ATM")
            break
        else:
            print("Invalid choice.Choose (1-4)")

miniatm()
            
    