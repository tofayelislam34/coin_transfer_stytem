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
    with open('login_data.json', 'r') as file:                   #context manager
        file_content = json.load(file)

    return file_content[0]['username']
