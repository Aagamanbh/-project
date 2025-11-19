masterpassword=input("Enter your master password: ")
def view():
    try:
         with open ("password.txt","r") as f:
             for line in f.readlines(): 
              data=line.strip()
             if "||" in data:
                    parts = data.split("||")
                    if len(parts) == 2:
                        account, password = parts
                        print(f"Name: {account} || Password: {password}")
                    else:
                        print(f"Line format error: {data}")
             else:
                    print(f"Invalid line format: {data}")
    except FileNotFoundError:
         print("Password doesnt exists. ")

def add():
    name=input("Enter Account name: ")
    password=input("Enter password: ")
    with open("Password.txt","a") as f:
        f.write(f"{name}||{password}\n")



while True:
    mode=input("Would you like to add password od view password(add/view),'q' for quit: ")
    if mode=="q":
        break
    
    if mode=="add":
        add()
    elif mode=="view":
        view()
    else:
        print("Invalid input.Enter add,view,q to quit.")