from deep_translator import GoogleTranslator
from functools import reduce
import pyfiglet
import os

class Update:
    def Main():

        # Declaring the variables
        Yes = "y"

        # Update the system
        os.system("echo {} |sudo pacman -Syyu".format(Yes))

        # These are the selections to choose from
        print("\nDo you want eraser cache?\n")
        print("1. Leave the three previous versions")
        print("2. Only leave a one version")

        while True:
            # This is the selection
            Option = input("\nType an option: ")

            if Option == "1":
                os.system("echo %s| sudo -S paccache -r\n" % Yes)
                os.system("echo %s" % Yes)
                break

            elif Option == "2":
                os.system("echo %s|sudo -S pacman -Scc\n" % Yes)
                os.system("echo %s" % Yes)
                break

            else:
                print("\nWrong choice")

class Translate:
    def Main():
        while True:
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
                break

            elif(Opcion == "2"):
                traductor = GoogleTranslator(
                                            source= Ingles, target= Español)
                resultado = traductor.translate(Texto)
                print("The translation from Spanish to English is: "
                        + resultado)
                break
                        
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
        Update.Main()
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

        while True:
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

            else:
                os.system("Wrone choice")

    elif(switch == "4"):
        print("Exiting...")
        os.system("clear")
        break

    else:
        print("Invalid option")
        os.system("clear")
