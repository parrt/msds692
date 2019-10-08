from getpass import getpass

def login():
    user = input("Enter your username: ")
    password = getpass()
    return user, password

if __name__ == '__main__':
    print(login())
