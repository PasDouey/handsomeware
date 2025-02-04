# Handsomeware - RSA File Encryption & Decryption

Handsomeware is a Python-based tool that encrypts and decrypts files using RSA encryption. It is designed to help users protect their sensitive text-based files by converting them into an encrypted format that can only be decrypted with a generated private key.

## Features
- Encrypts all files with a specified extension (default: `.txt`).
- Decrypts previously encrypted files.
- Automatically generates RSA key pairs.
- Saves the private key securely to `private_key.pem`.
- Uses secure OAEP padding for encryption.

## Requirements
This script requires Python 3 and the `cryptography` library.

### Install Dependencies
Run the following command to install the required package:
```bash
pip install cryptography
```

## Usage
### Encrypt Files
To encrypt all `.txt` files in the current directory, run:
```bash
python main.py encrypt
```

To specify a different file extension:
```bash
python main.py encrypt --extension .log
```

### Decrypt Files
To decrypt previously encrypted files, run:
```bash
python main.py decrypt
```

To specify a different file extension:
```bash
python main.py decrypt --extension .log
```

## How It Works
1. **Encryption Process:**
   - The script generates an RSA key pair.
   - It searches for files with the specified extension.
   - Each file is read and encrypted in chunks of 256 bytes.
   - The encrypted content replaces the original file.
   - The private key is saved in `private_key.pem`.

2. **Decryption Process:**
   - The script loads the RSA private key.
   - It finds encrypted files and decrypts them in 256-byte chunks.
   - The decrypted content replaces the encrypted file.

## Important Notes
- Keep `private_key.pem` safe. Without it, you cannot decrypt the files.
- Only files encrypted with this script can be decrypted.
- Do not modify encrypted files manually; it may cause decryption errors.
- The tool is intended for educational and security research purposes only.


