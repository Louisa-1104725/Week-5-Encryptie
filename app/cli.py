from cryptography.fernet import Fernet, InvalidToken


def cryptography_tool():
    print("Deze tool versleutelt een tekst en kan die direct weer ontsleutelen.")
    key = Fernet.generate_key()
    f = Fernet(key)
    plaintext = input("Voer de tekst in die je wilt versleutelen: ")
    plaintext_encode = plaintext.encode("utf-8")
    token = f.encrypt(plaintext_encode)
    print("Sleutel:", key)
    print("Token:", token)


if __name__ == "__main__":
    cryptography_tool()
