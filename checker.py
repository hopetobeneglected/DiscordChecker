import requests
from colorama import Fore
import os

if not os.path.exists("tokens.txt"):
    print(Fore.RED + "Please, create tokens.txt first!")

valid = []
invalid = []


def check_token(token: str):
    header = {
        "Authorization": token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    resp = requests.get(url="https://discord.com/api/v9/users/@me", headers=header)
    return resp


def check_all():
    with open("tokens.txt", "r") as f:

        tokens = f.read()

        print(Fore.BLUE + "Discord tokens validity check...\n")

        for token in tokens.split():
            print(Fore.YELLOW + "Checking... " + Fore.BLUE + token)

            resp = check_token(token)

            if resp.status_code == 200:
                valid.append(token)
                print(Fore.GREEN + token + " : Valid")
            else:
                invalid.append(token)
                print(Fore.RED + token + " : Invalid")


def delete_invalid():
    with open("tokens.txt", "w+") as f:
        for token in valid:
            f.write(token + "\n")


def get_info():
    check_all()
    print("\n" + Fore.RED + "Invalid tokens: " + Fore.BLUE + str(len(invalid)) + "\n")
    delete_invalid()
    print("All invalid tokens were successfully deleted from the tokens.txt file!\n")
    print(Fore.GREEN + "Valid tokens: " + Fore.BLUE + str(len(valid)))
    for i in valid:
        print(Fore.LIGHTWHITE_EX + i)


if __name__ == '__main__':
    get_info()
