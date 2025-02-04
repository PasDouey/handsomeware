import argparse
import os
from files_stuff import check_files_existence_in_direc, files_extension
from Key_generation import crypting_keys
from Crypt import encrypting
from Decrypt import decrypting
from cryptography.hazmat.primitives import serialization

# Encrypt files
def encrypt_txt_files(extension=".txt"):
    private_key, public_key = crypting_keys()
    files = check_files_existence_in_direc()
    txt_files = files_extension(files, extension)

    for file in txt_files:
        encrypting(file, public_key)

    # Save private key
    with open("private_key.pem", "wb") as key_file:
        key_file.write(
            private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            )
        )
    print("Private key saved to 'private_key.pem'")

# Decrypt files
def decrypt_txt_files(extension=".txt"):
    if not os.path.exists("private_key.pem"):
        print("Error: private_key.pem not found!")
        return

    with open("private_key.pem", "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None
        )

    files = check_files_existence_in_direc()
    txt_files = files_extension(files, extension)

    print(f"Files found for decryption: {txt_files}")  # DEBUG

    if not txt_files:
        print(f"No files found with extension '{extension}'.")
        return

    for file in txt_files:
        print(f"Decrypting: {file}")  # DEBUG
        decrypting(file, private_key)

    print(f"Files with extension '{extension}' decrypted.")

# Main execution
def main():
    parser = argparse.ArgumentParser(description="Encrypt or decrypt files using RSA.")
    parser.add_argument("action", choices=["encrypt", "decrypt"], help="Action to perform: 'encrypt' or 'decrypt'.")
    parser.add_argument("-e", "--extension", default=".txt", help="Specify the file extension to encrypt/decrypt (default: .txt).")

    args = parser.parse_args()

    if args.action == "encrypt":
        print(f"Encrypting files with extension '{args.extension}'...")
        encrypt_txt_files(args.extension)
    elif args.action == "decrypt":
        print(f"Decrypting files with extension '{args.extension}'...")
        decrypt_txt_files(args.extension)

# Run the script
if __name__ == "__main__":
    main()
