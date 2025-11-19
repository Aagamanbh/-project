"""
scissor=-1
paper=0
rock=1
"""
import random
choice={"scissor":-1,"paper":0,"rock":1}
reversechoice={-1:"scissor",0:"paper",1:"rock"}
while True:
        computer=random.choice([-1,0,1])
        yourchoice=input("Choose (scissor/paper/rock): ").lower()
        if yourchoice not in choice:
              print("Invalid.Choose between (scissor/paper/rock).")
              continue
            
        you=choice[yourchoice]
        print(f"=>You choose: {reversechoice[you]}, computer choose: {reversechoice[computer]}")
        if (you==computer):
           print("Its a draw!!")
        elif (you==0 and computer==1):
            print("You win!!")
        elif (you==-1 and computer==0):
            print("You win!!")
        elif (you==1 and computer==-1):
             print("You win!!")
        else:
              print("Computer win!!")

        play_again=input("Wanna play again?(yes/no): ").lower()
        if play_again!="yes":
         print("\nThankyou for playing!!")
         break