# RSA & AES Encryption/Decryption App

This application enables users to securely encrypt and decrypt messages using both RSA public key cryptography and AES symmetric key cryptography. It offers functionalities to generate RSA keys, encrypt messages with RSA public keys or AES keys, and decrypt them with the corresponding RSA private keys or AES keys. The addition of AES encryption provides a symmetric encryption option that is efficient for larger volumes of data.

## Features

- Generate RSA keys with selectable key sizes (2048, 3072, 4096 bits) for various security levels.
- Encrypt and decrypt messages using RSA public and private keys.
- Generate AES keys and initialization vectors (IV) for AES encryption.
- Encrypt and decrypt messages using AES with a key and IV.
- Simple and intuitive Streamlit interface for easy operation.

## Installation

To use this application, you'll need Python and Streamlit. Here are the steps to get set up:

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/ajanraj/RSA-Encryption_Decryption-WebApp.git
   ```

2. Navigate to the directory of the cloned repository:

   ```
   cd RSA-Encryption_Decryption-WebApp
   ```

3. Install the necessary Python packages:

   ```
   pip install -r requirements.txt
   ```

   This command installs Streamlit and PyCryptodome, the required libraries for the app.

## Running the Application

Launch the application using Streamlit with the following command:

```
streamlit run app.py
```

Adjust \`app.py\` to the correct path or name of the Python script if needed.

## Usage

1. **Generate RSA Keys**: Choose 'Generate RSA Keys' from the sidebar. Select a key size and click 'Generate Keys' to create a new RSA key pair.
2. **RSA Encrypt/Decrypt Message**: 
   - For encryption, upload your RSA public key, enter your message, and encrypt it.
   - For decryption, upload your RSA private key and the encrypted message to decrypt it.
3. **AES Encryption/Decryption**:
   - To encrypt, generate an AES key and IV, then enter your message for AES encryption.
   - To decrypt, enter the AES key and IV along with your encrypted message to decrypt it.

## Security Note

Keep your private keys and AES keys secure. Do not share them or upload them to untrusted platforms.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
