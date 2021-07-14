import json

file_name = 'login_data.json'

def load_file():
    with open(file_name, 'r+') as file:
        file_content = json.load(file)

    return file_content


class JsonClass:
    def __init__(self, file):
        self.file_name = file


    def json_load(self):
        with open(self.file_name, 'r+') as file:
            file_content = json.load(file)

        return file_content

    def json_dump(self,):
        with open(self.file_name, 'r+') as file:
            file_content = json.load(file)

        return file_content


files = JsonClass(file_name)


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
    # with open('login_data.json', 'r+') as file: #context manager
    #     file_content = json.load(file)

    for _ in files.json_load():
        if _['username'] == user:
            if _['password'] == password:
                print('confirmed user name. ')
                print('confirmed password')
                username = _['username']
                login_after_menu(username)
                break
    else:
        print('username/ password is incorrect')


def login_after_menu(name):
    print(f'welcome to our service MR. {name}')

    user_choice = input("""
        Enter A - For account Details
        Enter D - For Deposite Money
        Enter S - For send money
        Enter L - Logout
    """)
    while user_choice != 'l':
        if user_choice.lower() == 'a':
            account_details(name)
        elif user_choice == 'd':
            deposite_money()
        elif user_choice == 's':
            send_money()
        else:
            print('Unknown command, Please try again..!')

        user_choice = input("""
                Enter A - For account Details
                Enter D - For Deposite Money
                Enter S - For send money
                Enter L - Logout
            """)


def account_details(name):
    for _ in files.json_load():
        if _['username'] == name:
            print(
                f"""
                username:{_['username']}
                Email: {_['email']} 
                """
            )

    # login_after_menu(name)


