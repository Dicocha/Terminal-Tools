from deep_translator import GoogleTranslator
from cryptography.fernet import Fernet
from functools import reduce
import pyfiglet
import os

class Update:
    key = Fernet.generate_key()

    def Encrypt():
        # Opened the file Thekey.key to read the key
        with open("Thekey.key", "rb") as filekey: 
            key = filekey.read() 
        fernet = Fernet(key) 
            
        # Read the file to be encrypted
        with open("Password.txt", "rb") as file: 
            original = file.read()
            
        # Encrypted the file
        encrypted = fernet.encrypt(original) 
            
        # Write the encrypted file
        with open("Password.txt", "wb") as encrypted_file: 
            encrypted_file.write(encrypted)

    def Decrypt():
        # Opened the file Thekey.key to read the key
        with open("Thekey.key", "rb") as filekey: 
            key = filekey.read()

        # Reading the encrypted file
        with open("Password.txt", "rb") as enc_file: 
            Decrypt = enc_file.read()

        # Decrypt the file and retorned the text
        fernet = Fernet(key)
        decrypted = fernet.decrypt(Decrypt)
        return decrypted.decode()
        
    def Main():
        # Declaring the variables
        passw = Update.Decrypt()
        Yes = "y"

        # This is the error 
        os.system("echo %s |sudo -S pacman -Syyyyu" % passw)

        # These are the selections to choose from
        print("\nDo you want eraser cache?\n")
        print("1. Leave the three previous versions")
        print("2. Only leave a one version\n")

        # This is the selection
        Option = input("Type an option: ")

        if Option == "1":
            os.system("echo %s| sudo -S paccache -r\n" % Yes)
            os.system("echo %s" % Yes)

        elif Option == "2":
            os.system("echo %s|sudo -S pacman -Scc\n" % Yes)
            os.system("echo %s" % Yes)

        else:
            print("\nWrong choice")

    def Make_dir():
        os.mkdir("Resources")
        os.chdir("Resources")

        # Generate a key Fernet for encrypting password root
        global key
        key = Fernet.generate_key()
        with open("Thekey.key","wb") as File_key:
            File_key.write(key)

        password = input("Type the root pasword: ")

        with open("Password.txt","w") as File_key:
            File_key.write(password)

        Update.Encrypt()

class Translate:
    def Main():
        Opcion = input("Type an option: ")
        Texto = input("Type the word to traslate: ")
        Español = "es"
        Ingles = "en"

        if(Opcion == "1"):
            traductor = GoogleTranslator(
                                        source= Español, target= Ingles)
            resultado = traductor.translate(Texto)
            print("The translation from English to Spanish is: "
                    + resultado)

        elif(Opcion == "2"):
            traductor = GoogleTranslator(
                                        source= Ingles, target= Español)
            resultado = traductor.translate(Texto)
            print("The translation from Spanish to English is: "
                    + resultado)
                    
        else: 
            print("\nWrong choice")

class Calculator:
    def main():
        Numbers = []
        print("\nEn cada entrada introduce un numero, "
                + "cuando termines solo presiona enter\n")

        # This loops to add the numbers
        while True:
            Numbers.append(input("Type the numbers: "))
            if Numbers[-1] == "":
                break
        Numbers.pop()

        # This is for a insert the numbers in a list
        Final_list = [int(item) for item in Numbers]
        return Final_list

    def Sum(x,y):
        return x+y

    def Subtract(x,y): 
        return x-y

    def Multiplication(x,y): 
        return x*y

    def Division(x,y):
        return x/y

while True:
    os.system("clear")
    print(pyfiglet.figlet_format("Terminal tools"))

    print("1. Update")
    print("2. Translate")
    print("3. Calculator")
    print("4. Exit\n")

    switch = input("Type an option: ")

    if(switch == "1"):
        os.system("clear")

        try:
            os.chdir("Resources")

        except:
            Update.Make_dir()
        
        Update.Main()
        os.chdir("..")
        os.system("clear")

    elif(switch == "2"):
        os.system("clear")
        print("Welcome to translate\n")
        print("Which language do you want to translate?")
        print("1) Spanish - English")
        print("2) English - Spanish\n")

        Translate.Main()

        Siguiente = input("\nDo you want to do other translations? "
                            + "(y/n): ")
        if Siguiente == "n":
            os.system("clear")
        
    elif(switch == "3"):
        Numeros = []

        os.system("clear")
        print("Welcome to calculator\n")
        print("What operation do want to do? \n")

        print("1. Sum")
        print("2. Substract")
        print("3. Multiplication")
        print("4. Division\n")

        Respuesta = input("Type an option: ")

        if Respuesta == "1":
            print("The resul is: " + str(reduce(Calculator.Sum, Calculator.main())))
            Siguiente = input("\nDo you want to do other operations?"
                                + "(y/n): ")
            if Siguiente == "n":
                os.system("clear")

        elif Respuesta == "2":
            print("The resul is: " + str(reduce(Calculator.Subtract, Calculator.main())))
            Siguiente = input("\nDo you want to do other operations?"
                                + "(y/n): ")
            if Siguiente == "n":
                os.system("clear")

        elif Respuesta == "3":
            print("The resul is: " + str(reduce(Calculator.Multiplication, Calculator.main())))
            Siguiente = input("\nDo you want to do other operations?"
                                + "(y/n): ")
            if Siguiente == "n":
                os.system("clear")

        elif Respuesta == "4":
            print("The resul is: " + str(reduce(Calculator.Division, Calculator.main())))
            Siguiente = input("\nDo you want to do other operations?"
                                + "(y/n): ")
            if Siguiente == "n":
                os.system("clear")

        elif Respuesta == "5":
            os.system("clear")
            break

    elif(switch == "4"):
        print("Exiting...")
        os.system("clear")
        break

    else:
        print("Invalid option")
        os.system("clear")
