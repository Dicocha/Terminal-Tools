from deep_translator import GoogleTranslator
from cryptography.fernet import Fernet
from functools import reduce
import pyfiglet
import os

class Update:
    clave = Fernet.generate_key()

    def Encrypt():
        # Se abre el archivo clave.key para leer la clave
        with open('clave.key', 'rb') as filekey: 
            key = filekey.read() 
        fernet = Fernet(key) 
            
        # Se lee el archivo a encriptar
        with open('Password.txt', 'rb') as file: 
            original = file.read()
            
        # Se encripta el archivo
        encrypted = fernet.encrypt(original) 
            
        # Se escribe el archivo encriptado
        with open('Password.txt', 'wb') as encrypted_file: 
            encrypted_file.write(encrypted)

    def Decrypt():
        # Se abre el archivo clave.key para leer la clave
        with open('clave.key', 'rb') as filekey: 
            key = filekey.read()

        # Se lee el archivo a desencriptar
        with open('Password.txt', 'rb') as enc_file: 
            Decrypt = enc_file.read()

        fernet = Fernet(key)

        # Se desencripta el archivo y retorna el texto
        decrypted = fernet.decrypt(Decrypt)
        return decrypted.decode()
        
    def Actualizar():
        passw = Update.Decrypt()
        Respuesta = "y"

        os.system('echo %s |sudo -S pacman -Syyyyu' % passw)

        print("\n¿Desea borrar la cache de pacman?")
        print("\n1. Dejar las tres ultimas versiones")
        print("2. Dejar solamente la actual:\n")

        respuesta = input("Elegir una opcion: ")

        if respuesta == "1":
            os.system('echo %s| sudo -S paccache -r\n' % Respuesta)
            os.system('echo %s' % Respuesta)

        elif respuesta == "2":
            os.system('echo %s|sudo -S pacman -Scc\n' % Respuesta)
            os.system('echo %s' % Respuesta)

        else:
            print("\nRespuesta incorrecta")

    def Make_dir():
        os.mkdir("Recursos")
        os.chdir("Recursos")

        # Genera una clave Fernet para encriptar la clave root
        global clave
        clave = Fernet.generate_key()
        with open("clave.key","wb") as archivo_clave:
            archivo_clave.write(clave)

        password = input("Introducir la contraseña root: ")

        with open("Password.txt","w") as archivo_clave:
            archivo_clave.write(password)

class Translate:
    def main():
        Opcion = input("Introduce la opcion: ")
        Texto = input("Introducir palabras a traducir: ")
        Español = "es"
        Ingles = "en"

        if(Opcion == "1"):
            traductor = GoogleTranslator(source= Español, target= Ingles)
            resultado = traductor.translate(Texto)
            print("La traduccion al ingles es: " + resultado)

        else:
            traductor = GoogleTranslator(source= Ingles, target= Español)
            resultado = traductor.translate(Texto)
            print("La traduccion al ingles es: " + resultado)

class Calculator:
    def main():
        Numeros = []
        print("\nEn cada entrada introduce un numero, cuando termines solo presiona enter\n")

        while True:
            Numeros.append(input("Introduce los numeros: "))
            if Numeros[-1] == "":
                break
        Numeros.pop()

        Lista_final = [int(item) for item in Numeros]
        return Lista_final

    def Suma(x,y):
        return x+y

    def Resta(x,y): 
        return x-y

    def Multi(x,y): 
        return x*y

    def Div(x,y):
        return x/y

while True:
    os.system('clear')
    print(pyfiglet.figlet_format("Terminal tools"))

    print("1. Update")
    print("2. Translate")
    print("3. Calculator")
    print("4. Exit\n")

    switch = input("Seleccione una opcion: ")

    if(switch == "1"):
        os.system('clear')

        try:
            os.chdir("Recursos")

        except:
                Update.Make_dir()
        
        Update.Actualizar()
        os.chdir("..")
        os.system('clear')

    elif(switch == "2"):
        os.system('clear')
        print("Bienvenido al traductor\n")
        print("Que idioma quiere traducir:")
        print('1) Español - Ingles')
        print('2) Ingles - Español\n')

        Translate.main()

        Siguiente = input("\nDesea realizar otra traduccion? (y/n): ")
        if Siguiente == "n":
            os.system('clear')
        
    elif(switch == "3"):
        Numeros = []

        os.system('clear')
        print("Bienvenido a la calculadora\n")
        print("Que operacion desea realizar: \n")

        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division\n")

        Respuesta = input("Elija una opcion: ")

        if Respuesta == "1":
            print("El resultado es:" + str(reduce(Calculator.Suma, Calculator.main())))
            Siguiente = input("\nDesea realizar otra operacion? (y/n): ")
            if Siguiente == "n":
                os.system('clear')

        elif Respuesta == "2":
            print("El resultado es:" + str(reduce(Calculator.Resta, Calculator.main())))
            Siguiente = input("\nDesea realizar otra operacion? (y/n): ")
            if Siguiente == "n":
                os.system('clear')

        elif Respuesta == "3":
            print("El resultado es:" + str(reduce(Calculator.Multi, Calculator.main())))
            Siguiente = input("\nDesea realizar otra operacion? (y/n): ")
            if Siguiente == "n":
                os.system('clear')

        elif Respuesta == "4":
            print("El resultado es:" + str(reduce(Calculator.Div, Calculator.main())))
            Siguiente = input("\nDesea realizar otra operacion? (y/n): ")
            if Siguiente == "n":
                os.system('clear')

        elif Respuesta == "5":
            os.system('clear')
            break

    elif(switch == "4"):
        print("Exiting...")
        os.system("clear")
        break

    else:
        print("Invalid option")
        os.system("clear")
