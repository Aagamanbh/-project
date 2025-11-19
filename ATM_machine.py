print( """   \t ATM OF
SBL(Siddharth Bank Limited)""")

Balance=50000

while True:
    Choice=input("""
1.Check Balance
2.Deposit Amount
3.Withdraw Amount
4.End
Choose between (1-4):""")

    if Choice=="1":
          print(f"Total Balance is {Balance}")
    elif Choice=="2":
        amount=int(input("How much amount You want to deposit: "))
        if (amount>0):
            Balance+=amount
            print(f"Balance after Deposit is: {Balance}")
        else:
            print("Entered amount is negative.")
    elif Choice=="3":
        amount=int(input("How much amount you want to withdraw: "))
        if (Balance>=amount and amount>0):
            Balance-=amount
            print(f"Balance after withdraw is: {Balance}")
        else:
            print("Insufficient Balance to Withdraw")
    elif Choice=="4":
        print("Thank-you><Hope you are satisfied with our service.")
        break
    else:
         print("You Entered  Choice(1-4) is incorrect.Please enter 1 or 2 or 3 or 4 .")


