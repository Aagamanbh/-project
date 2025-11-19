"""
snake =-1
water=0
gun=1

"""
import random
choice={"snake":-1,"water":0,"gun":1}
reversechoice={-1:"Snake",0:"Water",1:"Gun"}

while True:
    computer=random.choice([-1,0,1])
    yourchoice=input("Enter your choice:(snake/water/gun):").lower()
    if yourchoice not in choice:
        print("Invalid choice,Choose any one of them(snake/water/gun):")
    you=choice[yourchoice]
    print(f"You choose {reversechoice[you]} and\nComputer choose {reversechoice[computer]}")
    if(you==computer):
        print("Its a draw!")
    else:
        if(you==-1 and computer==0):
            print("You Won!")
       
       
        elif(you==0 and computer==1):
            print("You Won!")
        elif(you==1 and computer==-1):
            print("You Won!")
       
        else:
            print("Computer Won!!!")

    playagain=input("Wanna play again??(yes/no): ")
    if playagain!="yes":
        print("Thankyou for playing!!")
        break
