import os

print("Welcome to an installation of requirements" 
        + " of the program Terminal-Tools\n")

Respuesta = input("You can install of requirementes? (y/n): ")

while True:
    if Respuesta == "y":
        os.system("pip install pyfiglet==0.7")
        os.system("pip install deep-translator")
        os.system("pip install pyperclip")

    else:
        print("\nYou have not installed the requirements\n")
        break