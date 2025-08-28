# import json

def auth_user(username, password):
    if (username == "admin" and password == "123"):
        return True
    return False


if __name__ == '__main__':
    print(auth_user("admin", "123") )