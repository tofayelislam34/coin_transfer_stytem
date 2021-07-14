import json

file_name = 'login_data.json'


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


def send_money():
    total_tk = 1000000
    tk = int(input("Enter amount you want to sent: "))
    print(f"your previous tk was:${total_tk} ")
    remaining_tk = total_tk - tk
    print(f"After send you have :${remaining_tk}")


