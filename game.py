"""
Pikaachu's Adventure
Edro Gonzales A01257468
Ian Chan A00910012
"""
import json
import os

def get_name():
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
    print("\033[92mNew users: please remember your chosen username for future sessions\033[0m")
    print(
        "\033[94mAfter entering your username, press your 'Enter' key to continue and head over to the window "
        "screen.\033[0m")
    user_name = input("Please select a name young trainer: ")
    return user_name

def generate_character_info(name):
    """
    Generates character information.

    :param name: string name of character
    :precondition: name must be a string of characters representing username
    :postcondition: makes a dictionary containing information of character
    :postcondition: saves that dictionary into a JSON file for future use
    :return: dictionary of character information
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

def main():
    trainer_name = get_name()

    character_info = generate_character_info(trainer_name)

    print(character_info)

if __name__ == '__main__':
    main()