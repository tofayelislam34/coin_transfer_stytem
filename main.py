# TODO: user have to create an account
# TODO: if the user already have a account then he/ she have ot login first
# TODO: if login then,
"""
- Deposite money
- Send money
- Account information
- Reset Password
- Exit
"""
#TODO: we will add more functionality to this system. like, user can sent money to another user .


def menu():
    print('Welcome to our money transfer system! (P-pay) ')

    user_input = input("""
        - Create Account. Enter 'C' to Create account
        - Already have account? then press 'L' to login.
        - Press 'E' to Exit
    """)
    while user_input != 'q':

        if user_input == 'c':
            create_account()
        elif user_input == 'l':
            login()
        else:
            print('Unknown Command! please try again..')

        user_input = input("""
                - Create Account. Enter 'C' to Create account
                - Already have account? then press 'L' to login.
                - Press 'E' to Exit
            """)


menu()