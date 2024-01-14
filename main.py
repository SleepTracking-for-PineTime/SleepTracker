import os
import sys
import pickle

def help():
    print("\nCommands:")
    print("help     Display the list of available commands.")
    print("connect  Connect with pinetime then collect the data from your watch in the data folder.")
    print("analysis Generate a graph of the backup you select.")
    print("profile  Allows you to personalize the analysis according to your age and any pathology having consequences on your sleep.\n")

def connect():
    print("in development")

def analysis():
    print("in development")

def new_profile():
    try:
        os.remove("data/.profile")
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"An error occurred while deleting the file: {e}")
    try:
        with open("data/.profile", "wb") as file:
            name = str(input("1. Choose a name for your profile: "))
            age = int(input("2. How old are you? [0/100]: "))
            health = str(input("3. Do you have an illness that affects your sleep? [y/n]: ").lower())
            
            if health == "y":
                health = True
            elif health == "n":
                health = False
            else:
                print("Please start again.")
                return
            
            dictionary = {
                "Name": name,
                "Age": age,
                "Health": health
            }

            pickle.dump(dictionary,file)
            file.close()

    except Exception as e:
        print(f"An error occurred while creating the file: {e}")

def profile():
    if os.path.exists("data/.profile"):
        confirmation = input(f"A profile already exists, do you want to replace it? [y/N]: ").lower()

        if confirmation != 'y':
            print("Operation canceled.")
            return
        else:
            new_profile()
    else:
        new_profile()

commands = {
    "help": help,
    "connect": connect,
    "analysis": analysis,
    "profile": profile
}

def main():
    argc = len(sys.argv)

    if argc < 2:
        print("Usage: python main.py <command>.")
    else:
        query = sys.argv[1]

        if query in commands:
            commands[query]()
        else:
            print(f"No function associated with '{query}'.")
            print("If you need help enter the 'help' argument.")

if __name__ == "__main__":
    main()