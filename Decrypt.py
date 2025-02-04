from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import os

def decrypting(filename, private_key):
    with open(filename, "rb") as file:
        encrypted_data = file.read()

    chunk_size = 256  # Taille d'un bloc RSA 2048
    decrypted_chunks = []

    # Vérifie que la taille est bien un multiple de 256
    if len(encrypted_data) % chunk_size != 0:
        print(f"Error: Encrypted file '{filename}' is not correctly chunked.")
        return

    try:
        for i in range(0, len(encrypted_data), chunk_size):
            chunk = encrypted_data[i:i+chunk_size]
            decrypted_chunk = private_key.decrypt(
                chunk,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            decrypted_chunks.append(decrypted_chunk)

        # Reconstruire le fichier original
        with open(filename, "wb") as file:
            for chunk in decrypted_chunks:
                file.write(chunk)

        print(f"File '{filename}' decrypted successfully.")

    except ValueError as e:
        print(f"Error decrypting '{filename}': {e}")
