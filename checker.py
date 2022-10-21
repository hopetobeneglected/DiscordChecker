import requests
from colorama import Fore
import os

if not os.path.exists("tokens.txt"):
    print(Fore.RED + "Please, create tokens.txt first!")

valid = []
invalid = []


def check_tokens():
    with open("tokens.txt", "r") as f:
        tokens = f.read()
        for token in tokens.split():
            print(Fore.YELLOW + "Checking... " + Fore.BLUE + token)

            headers = {
                "Authorization": token,
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
            }

            resp = requests.get(url="https://discord.com/api/v9/users/@me", headers=headers)

            if resp.status_code == 200:
                valid.append(token)
                print(Fore.GREEN + token + " : Valid")
            else:
                invalid.append(token)
                print(Fore.RED + token + " : Invalid")


def get_info():
    check_tokens()
    print()
    print(Fore.RED + "Invalid tokens: " + Fore.BLUE + str(len(invalid)))
    print()
    for i in valid:
        print(Fore.GREEN + "Valid tokens: " + Fore.BLUE + str(len(valid)))
        print(Fore.LIGHTWHITE_EX + i)


if __name__ == '__main__':
    get_info()
