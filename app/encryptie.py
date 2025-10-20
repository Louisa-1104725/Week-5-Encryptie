import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet, InvalidToken

def cryptography_tool():
    load_dotenv()
    key = os.getenv('FERNET_KEY')
    if not key:
        print('Fernet key niet gevonden, voeg FERNET_KEY toe')
        return

    try:
        f = Fernet(key.encode("utf-8"))
    except (ValueError, TypeError):
        print ('FERNET_KEY in .env is ongeldig')
        return

    while True:
        print("Deze tool versleutelt een tekst en kan die weer ontsleutelen.")
        option = input("Wil je een tekst versleutelen (1), ontsleutelen (2) of stoppen (Q)?").lower()

        if option == "1":
            plaintext = input("Voer de tekst in die je wilt versleutelen: ")

            #Invoer wordt versleuteld met een fernet-key en weergegeven aan de gebruiker.
            plaintext_encode = plaintext.encode("utf-8")
            token = f.encrypt(plaintext_encode)
            print("Sleutel: zie .env voor de sleutel")
            print("Token:", token.decode())

            choice = input("Wil je direct weer ontsleutelen? (j/n): ").lower()
            if choice == "j" or choice == "ja":
                #Token wordt weer ontsleuteld met de fernet-key.
                decrypted: bytes = f.decrypt(token)
                text = decrypted.decode("utf-8")
                print(f"Ontsleutelde tekst: {text}")
                print("-----------------------------------------")
            elif choice == "n" or choice == "nee":
                continue

        elif option == "2":
            print("Je hebt gekozen voor ontsleutelen.")
            token = input("Plak hier de token: ").strip()

            #Er wordt gecontroleerd of de token voldoet aan utf-8.
            try:
                plaintext = f.decrypt(token.encode("utf-8"))
            # Als het een ongeldige invoer is, wordt de error afgevangen.
            except InvalidToken:
                print("Fout: ongeldige token.")
                print("-----------------------------------------")
                continue

            #Als alles klopt, wordt het bericht ontsleuteld.
            text = plaintext.decode("utf-8")
            print(f"Ontsleutelde tekst: {text}")
            print("-----------------------------------------")
            continue

        elif option == "q":
            break
        else:
            print("Fout: ongeldige invoer. Je kan alleen kiezen uit 1, 2 of Q")
            print("-----------------------------------------")
            continue

if __name__ == "__main__":
    cryptography_tool()
