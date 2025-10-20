import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet, InvalidToken

def key_generator():
    with open(".env", "w") as f:
        f.write(f"FERNET_KEY={Fernet.generate_key().decode()}")
    print("Nieuwe Fernet-sleutel opgeslagen in .env")
    print("Start applicatie handmatig opnieuw op")

def cryptography_tool():
    load_dotenv()
    key = os.getenv('FERNET_KEY')
    if not key:
        print("ontbrekende FERNET-KEY, aanmaken FERNET-KEY.. ")
        key_generator()
        return

    try:
        f = Fernet(key.encode("utf-8"))
    except (ValueError, TypeError):
        print ('FERNET_KEY in .env is ongeldig')
        return

    while True:
        print("Deze tool versleutelt een tekst en kan die weer ontsleutelen.")
        option = input("Wil je een tekst versleutelen (1), ontsleutelen (2), nieuwe key (3) of stoppen (Q)?").lower()

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

        elif option == "3":
            print("Als je een nieuwe key genereert, dan kunnen alle huidige versleutelde berichten niet meer ontsleuteld worden.")
            verification = input("Wil je doorgaan? (j/n)").lower()
            if verification == "j" or verification == "ja":
                key_generator()
                print("Nieuwe FERNET-KEY is aangemaakt")
            elif verification == "n" or verification == "nee":
                print("Terug naar startscherm")
                print("-----------------------------------------")
                continue
            else:
                print("Fout: ongeldige invoer. Terug naar startscherm")
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
