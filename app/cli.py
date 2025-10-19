from cryptography.fernet import Fernet, InvalidToken

def cryptography_tool():
    key = Fernet.generate_key()
    f = Fernet(key)
    while True:
        print("Deze tool versleutelt een tekst en kan die weer ontsleutelen.")
        option = input("Wil je een tekst versleutelen (1), ontsleutelen (2) of stoppen (Q)?")

        if option == "1":
            plaintext = input("Voer de tekst in die je wilt versleutelen: ")

            #Invoer wordt versleuteld met een fernet-key en weergegeven aan de gebruiker.
            plaintext_encode = plaintext.encode("utf-8")
            token = f.encrypt(plaintext_encode)
            print("Sleutel:", key)
            print("Token:", token)

            choice = input("Wil je direct weer ontsleutelen? (j/n): ").lower()
            if choice == "j" or choice == "ja":
                #Token wordt weer ontsleuteld met de fernet-key.
                decrypted: bytes = f.decrypt(token)
                text = decrypted.decode("utf-8")
                print("Ontsleutelde tekst:")
                print(text)
                print("-----------------------------------------")
            elif choice == "n" or choice == "nee":
                continue

        elif option == "2":
            print("Je hebt gekozen voor ontsleutelen.")
            key = input("Plak hier de sleutel: ").strip()
            token = input("Plak hier de token: ").strip()

            #Er wordt gecontroleerd of de fernet-key voldoet aan utf-8.
            try:
                f = Fernet(key.encode("utf-8"))
            #Als het een ongeldige invoer is, wordt de error afgevangen.
            except (ValueError, TypeError):
                print("Fout: ongeldig formaat sleutel.")
                print("-----------------------------------------")
                continue

            #Er wordt gecontroleerd of de token voldoet aan utf-8.
            try:
                plaintext = f.decrypt(token.encode("utf-8"))
            # Als het een ongeldige invoer is, wordt de error afgevangen.
            except InvalidToken:
                print("Fout: ongeldige token of verkeerde sleutel.")
                print("-----------------------------------------")
                continue

            #Als alles klopt, wordt het bericht ontsleuteld.
            try:
                print(" Ontsleutelde tekst: ")
                print(plaintext.decode("utf-8"))
            except UnicodeDecodeError:
                print("Ontsleutelde bytes: ")
            print(plaintext)
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
