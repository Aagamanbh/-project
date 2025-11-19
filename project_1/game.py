print("Welcome to my Game.")
name=input("Enter your name:")
age=int(input("Enter your age:"))
if age>=18:
    print("You meet the requirement to play game.")

    wants_to_play=input("Do You want to play the game(yes/no)? ").lower()
    if wants_to_play=="yes":
         print("Lets Begin!!")
         health=10
         start=(f"You are starting with {health} health.")
         print(start)
         ask=input("Welcome to the game,Now choose left or right(left/right):").lower()
         if ask=="left":
             print("Congratulation.You reached the basecamp from where you can climb MountEverest....\n")
             ask=input("Choose whether to climb using (rope/stairs) ").lower()
             if ask=="rope":
                 print("You have reached 2000 m above the base.\n")
                 ask=input("Do you want to give up or climb (climb/giveup):").lower()
                 if ask=="climb":
                     health-=4
                     print(f"\nYou have reached 6000 m but while climbing you lost oxygen cylinder and you lost your health... Now you have {health} health remaining\n")
                     ask=input("You are just 2800m down to reach top..Will you like to continue climbing as you are sort of oxygen? " ).lower()
                     if ask=="yes":
                         print("Congratulations..You have reached the top.\nYou Winnnn!!!!")
                     if ask=="no":
                         print("As you were sort of oxygen cylinder... you died..\nYou loose!!")
                 if ask=="giveup":
                     print("You loose!!..As you have gaven up.")
             if ask=="stairs":
                 print("Your Stairs break and you fall down..And \nYou loose:( ")
         if ask=="right":
             health-=3
             print(f"\nWe were planing to climb the Mt Everest but you are late as per out schedule....Bus has already reaches the base camp..Now you have to walk for 5 hours to reach basecamp....\n")
             ask=input(f"You have reached the basecamp late so you lost health and now you have {health} health...Now Choose how you like to climb everst using path (easy /hard): ").lower()
             if ask=="easy":
                 print("You choose easy way ... this way contains lake...you fell in a lake and died.\n You Lose!!")
             if ask=="hard":
                 health-=2
                 print(f"You reached 1000m above basecamp but you lost your oxygen cylinder so you lost your {health} health\n")
             else:
                 print("You havent choosed the option.")
                 ask=input("Do you want to stop climbing for today (sleep/climb): ").lower()
                 if ask=="sleep":
                     print("While sleeping landslide kill you.\nYou loose!!")
                 if ask=="climb":
                     print("You have reached 1500 m above..but you cannot breath and died.\nYou loose!")
                 else:
                     print("You havent choosed the correct option ")
                

                
         
    else:
        print("Thank-you for visiting my game.. :)")
else:
    print(f"You are not eligible beacuse you are {age}")
