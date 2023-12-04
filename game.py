"""
Pikaachu's Adventure
Edro Gonzales A01257468
Ian Chan A00910012
"""

def get_name():
    """
    Gets name of user.

    :postcondition: user is prompted for username
    :return: string representing the typed username of user
    """
    print("""Enter your username. Using the same name retrieves your previous data.
    from unittest.mock import patch""")
    user_name = input("Please select a name young trainer: ")
    return user_name

def main():
    trainer_name = get_name()

if __name__ == '__main__':
    main()