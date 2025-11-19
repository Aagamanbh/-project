import random
while True:
    number=input("Enter a maximum number for guessing range:")
    if number.isdigit():
        number=int(number)
        if number<0:
            print("Enter number greater then Zero.")
            continue
            
    else:
        print("Enter the number next time. ")
        continue
    randomno=random.randint(0,number)
    guesses=0
    while True:
        guesses+=1
        guess=input("Enter guess: ")
        if guess.isdigit():
            guess=int(guess)
        else:
            print("Invalid input.Please enter a number.")
            continue
        if guess==randomno:
            print("You get it!")
            break
        elif guess<randomno:
            print("You are lower than number.")
            
        else:
            print("You are above than number.")     

    print(f"You got the number in {guesses} guess.")   


    play_again=input("Do you wanna play again? (yes/no) ").lower()
    if play_again not in ["yes","y"]:
        print("Thanks for playing! Goodbye.")
        break
        
    