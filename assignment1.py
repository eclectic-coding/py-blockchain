def get_user_name():
    get_name = input('Enter your name: ')
    return get_name


def get_user_age():
    get_age = input('Enter your age: ')
    return get_age


user_name = get_user_name()
user_age = get_user_age()

print("Hello " + user_name + ", you are " + user_age + " years old.")
