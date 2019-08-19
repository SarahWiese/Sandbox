"""Sarah Wiese"""
MIN_LENGTH = 5


def main():
    """Program to get and check users password"""
    password = input(">>> ")
    print("Enter a valid password: ")
    while not is_valid_password(password):
        print("Password must be {} character long".format(MIN_LENGTH))
        password = input(">>> ")
    for i in range(len(password)):
        s = "*"
    print(i * s)


def is_valid_password(password):
    """Check if passowrd is valid."""
    if len(password) <= MIN_LENGTH:
        return False
        print("Password must be {} characters long".format(MIN_LENGTH))
        password = input(">>> ")
    return True