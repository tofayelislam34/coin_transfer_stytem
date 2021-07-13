import json


def create(user, email, phone, password):

    program_list = {
           'username': user,
           'email': email,
           'number': phone,
           'password': password
    }

    with open('login_data.json', 'r+') as file:
        data = json.load(file)
        data.append(program_list)
        file.seek(0)
        json.dump(data, file)


def login(user, password):
    with open('login_data.json', 'r') as file:  #context manager
        file_content = json.load(file)

    for _ in file_content:
        if _['username'] == user:
            if _['password'] == password:
                print('confirmed user name. ')
                print('confirmed password')
                username = _['username']
                login_after_menu(username)
                break
    else:
        print('username / password is incorrect')


def login_after_menu(name):
    print(f'welcome Mr.{name}')
    print('Welcome to our system. Thank you for chossing our system')
    user_choice = input("""
        Enter A - for Account Information
        Enter D - For Deposite money
        Enter S - For Send money
        Enter L - For Logout
    """)

    while user_choice.lower() != 'l':
        if user_choice.lower() == 'a':
            account_info(name)
        elif user_choice.lower() == 'd':
            deposite_money()
        elif user_choice.lower() == 's':
            send_money()
        else:
            print('Unknown command. please try again!...')

        user_choice = input("""
                Enter A - for Account Information
                Enter D - For Deposite money
                Enter S - For Send money
                Enter L - For Logout
            """)

    print(f"Thanks Mr.{name}.Come again")


def account_info(name):
    with open('login_data.json', 'r+') as file:
        file_content = json.load(file)

    for _ in file_content:
        if _['username'] == name:
            print(f"""
            Name: {_['username']}
            Email: {_['email']}
            """)


def send_money():
    tk = input('Amount of money you want to send: ')














