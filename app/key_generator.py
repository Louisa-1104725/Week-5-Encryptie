from cryptography.fernet import Fernet

print(f"Fernet-key: {Fernet.generate_key().decode()}")
print("Je kan deze key gebruiken ipv de huidige key in de .env")