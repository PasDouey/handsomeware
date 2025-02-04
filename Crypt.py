from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import os

def encrypting(filename, public_key):
    with open(filename, "rb") as file:
        plaintext = file.read()
    
    max_length = 190  # RSA 2048 bits - padding
    encrypted_chunks = []

    for i in range(0, len(plaintext), max_length):
        chunk = plaintext[i:i+max_length]
        encrypted_chunk = public_key.encrypt(
            chunk,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        encrypted_chunks.append(encrypted_chunk)

    with open(filename, "wb") as file:
        for chunk in encrypted_chunks:
            file.write(chunk)
    
    print(f"File '{filename}' encrypted successfully.")
