from cryptography.fernet import Fernet

# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key","wb") as key_file:
#         key_file.write(key)
# write_key()

def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key


master_pswd = input("Enter master password: ")
key = load_key() # + master_pswd.encode()
fer = Fernet(key)

def view():
    with open("passwords.txt","r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user ,passw = data.split("|")
            print(f"Username: {user} | Password: {fer.decrypt(passw.encode()).decode()}")
def add():
    user = input("enter your username: ")
    pswd = input("enter your password: ")
    with open("passwords.txt","a") as f:
        f.write(f"{user}|{fer.encrypt(pswd.encode()).decode()}\n")
while True:
    mode = input("Do you want to add a new password or view existing passwords? (add/view or quit) ").lower()
    if mode == "quit":
        print("Goodbye!")
        exit()
    elif mode == "view":
        view()
    elif mode == "add":
        add()    