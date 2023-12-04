"""
Pikachu's Adventure
Edro Gonzales A01257468
Ian Chan A00910012
"""
import json
import os

def get_name() -> str:
    """
    Gets name of user.

    :postcondition: user is prompted for username
    :return: string representing the typed username of user
    """
    print("""
    ⠈⣿⣷⣶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠸⣿⣿⣿⣿⠈⠙⠲⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣶⣶⣶⡶⠀⠀⠀⠀⠀⠀
    ⠀⠀⠘⣿⣿⣿⡄⠀⠀⠀⠉⠲⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠔⠚⠉⠀⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠈⢿⣿⡧⠀⠀⠀⠀⠀⠀⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠞⠉⠀⠀⠀⠀⢠⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠙⣿⡖⠀⠀⠀⠀⠀⠀⠀⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠴⠉⠀⠀⠀⠀⠀⠀⢠⣾⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠉⠻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠱⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⢢⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠈⢧⠀⠀⢀⣠⠤⠴⠒⠒⠒⠒⠒⠒⠒⠲⠤⢤⣀⡀⢀⠜⠁⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⢀⣀⣠⠤⠔⠒⠉⠉⢸
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⢤⡀⠀⠀⠀⠀⠀⠈⠳⠊⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠋⠀⠀⠀⠀⠀⠀⠀⣀⡤⠚⠉⠀⠀⣀⡤⠔⠚⠉⠁⠀⠀⠀⠀⠀⠀⠸
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠲⢄⣀⢀⠖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⣀⣠⠴⠚⠁⢀⣠⠴⠒⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣄⣤⠔⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠃
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⡀⠀⠀⠀⢼⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⢸⣾⣿⢉⠈⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡏⠀⢹⣿⣦⡀⠀⢸⣟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠀⠀⠸⣿⣿⣷⣾⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⣿⣶⣿⣿⡿⠀⠀⠐⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⠤⠖⠃⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡇⠀⠀⠀⠙⠛⠛⠋⠀⠀⠀⠀⠀⠀⠘⠓⠀⠀⠀⠀⠀⠈⠛⠛⠋⠁⠀⠀⠀⢻⡀⠀⠀⠀⣀⣀⣀⡤⠤⠒⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠿⣿⢶⣄⠀⠀⠀⠀⢀⡀⠀⠀⠀⣀⣀⠀⠀⠀⠀⡀⠀⠀⠀⠀⢀⣴⣶⣶⣾⡇⠀⠀⠘⢫⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣯⢿⣝⣯⢿⣆⠀⠀⠀⠀⠙⠒⠒⠋⠉⠈⠙⠒⠒⠋⠀⠀⠀⠀⣰⣿⣻⢮⡷⢯⡗⠀⠀⠀⠀⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡿⢮⣻⣽⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣯⢷⣯⣟⣿⠃⠀⠀⠀⠀⠀⠀⠱⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠯⢷⢾⡿⠉⠓⠦⣄⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⠓⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠴⠻⡁⠀⣀⠴⠋⠁⠀⠀⠀⢀⣀⡤⠟⠃⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇⠀⠀⠈⠓⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠴⠚⠁⠀⠀⣷⠋⠁⠀⠀⣀⣠⠴⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⠀⠀⠀⠀⠀⠀⠀⠁⠈⠲⠶⣦⡄⣀⠤⠤⠀⢐⠛⠁⠀⠀⠀⠀⠀⠀⠹⡄⢀⢦⣻⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢆⡀⠀⠀⠀⠀⠀⢠⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣮⣟⣽⣿⡦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡇⠀⠀⠀⠀⢀⡎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠀⠀⠀⠀⣸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠱⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡃⠀⠀⢠⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡄⠀⠀⠀⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⠀⠀⠀⢹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣾⢺⠛⠢⣼⠁⠀⠀⠸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢺⠃⠀⠀⠀⠀⡇⢀⣠⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢿⢯⡳⡀⠈⠑⢆⠀⠀⠹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⣀⣀⢸⠃⠀⠀⠀⠀⠀⠀⠀⠀⢠⠏⠀⠀⠀⢀⡴⠛⢉⣼⣽⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠳⡽⠘⠓⢦⣀⠀⠀⠀⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⣸⠂⠀⠀⠀⠀⠀⠀⠀⢠⠟⠀⠀⠀⠴⣋⡠⠔⣺⣻⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢶⡀⠀⠈⠳⣄⠀⢀⠹⣄⠀⠀⠀⠀⠀⠀⠀⢰⡇⠀⠀⠹⡇⠀⠀⠀⠀⠀⠀⢠⡞⠄⠀⠀⣠⠞⠁⢀⣼⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢖⡂⡀⠈⠁⢿⠀⠙⢦⡀⠀⠀⠀⠀⠀⣼⣄⣦⣴⣥⡷⠀⠀⠀⠀⠀⣠⠋⠀⣄⠑⠘⠁⢀⣠⠿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠶⣖⣢⡾⠾⠴⠚⢳⣦⣠⣤⡶⠶⠛⠀⠀⠀⠘⠲⡤⣄⣀⣀⡞⠳⢤⣶⡏⣀⣠⡷⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        """)
    print("Welcome to Pikachu's Adventure!")
    print("Enter your username. If you've played before, use the same name to access your previous data.")
    print("\033[92mNew users: please remember your chosen username for future sessions.\033[0m")
    print(
        "\033[94mAfter entering your username, press your 'Enter' key to continue and head over to the window "
        "screen.\033[0m")
    user_name = input("Please type in a name: ")
    return user_name

def generate_character_info(name: str) -> dict:
    """
    Generates character information.

    :param name: string name of character
    :precondition: name must be a string of characters representing username
    :postcondition: makes a dictionary containing information of character
    :postcondition: saves that dictionary into a JSON file for future use
    :return: dictionary of character information

    >>> generate_character_info("test_user")
    {'name': 'test_user', 'health': 100, 'coordinates': (2, 1), 'skill': 'tackle', 'attack_power': 10, 'defense': 10, 'keys': 0, 'total_experience': 0}

    >>> generate_character_info("xxxxxxxxxx")
    {'name': 'xxxxxxxxxx', 'health': 100, 'coordinates': (2, 1), 'skill': 'tackle', 'attack_power': 10, 'defense': 10, 'keys': 0, 'total_experience': 0}
    """
    character_info = {
        "name": name,
        "health": 100,
        "coordinates": (2, 1),
        "skill": "tackle",
        "attack_power": 10,
        "defense": 10,
        "keys": 0,
        "total_experience": 0
    }

    file_name = os.path.join("saved", f"{name}_info.json")
    with open(file_name, "w") as file:
        json.dump(character_info, file, indent=4)

    return character_info

def user_has_file(name: str) -> bool:
    """
    Determines if user has a saved file or not.

    :param name: string representing the username
    :precondition: name must be a string representing the username typed by the user
    :postcondition: looks into saved folder and determines if the relevant file exists or not
    :return: True if json file exists or False otherwise

    >>> user_has_file("user_exist")
    True

    >>> user_has_file("user_does_not_exist")
    False
    """
    file_path = os.path.join("saved", f"{name}_info.json")
    return os.path.exists(file_path)

def main():
    trainer_name = get_name()

    user_has_profile = user_has_file(trainer_name)
    character_info = {}
    if not user_has_profile:
        character_info = generate_character_info(trainer_name)
    elif user_has_profile:
        # add get character info
        pass

if __name__ == '__main__':
    main()