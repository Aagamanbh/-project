print("Welcome, to my Quiz game.")
play=input("Do you wann play(yes/no)? ").lower()
 
if play=="yes":
    score=0
    qsn=input("What does GUI stands for? ").lower()
    if qsn=="graphical user interface":
        print("Correct!")
        score+=1
        
    else:
        print("Incorrect")

    qsn=input("What does CPU stands for? ").lower()
    if qsn=="central processing unit":
        print("Correct!!")
        score+=1
    else:
        print("Incorrect!!")
        print(f"You score is {score} and you have secured {(score/2)*100}%")
else:
    print("Thank-you for visiting this game.")
 

