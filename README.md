
# RSA Encryption/Decryption App

This application allows users to securely encrypt and decrypt messages using RSA public key cryptography. It provides functionality to generate RSA keys, encrypt messages with a public key, and decrypt them with a private key.

## Features

- Generate RSA keys with selectable key sizes (2048, 3072, 4096 bits) for varying levels of security.
- Encrypt messages using a provided RSA public key.
- Decrypt messages using a provided RSA private key.
- Simple and user-friendly Streamlit interface.

## Installation

To run this application, you will need Python and Streamlit. Follow these steps to set up the environment:

1. Clone this repository to your local machine:

```
git clone <repository-url>
```

2. Navigate to the cloned repository's directory:

```
cd <repository-name>
```

3. Install the required Python packages:

```
pip install -r requirements.txt
```

This command will install Streamlit and PyCryptodome, which are required for the application to run.

## Running the Application

After installing the required packages, you can run the application using Streamlit:

```
streamlit run app.py
```

Replace `app.py` with the path to the Python script if it's located in a different directory or has a different name.

## Usage

1. **Generate RSA Keys**: Select 'Generate Keys' from the sidebar and choose a key size. Click 'Generate Keys' to create a new pair of RSA keys.
2. **Encrypt Message**: Upload your public key, input your message, and encrypt it.
3. **Decrypt Message**: Upload your private key and the encrypted message to decrypt it back to plain text.

## Security Note

Always keep your private key secure. Do not share it with anyone or upload it to untrusted platforms.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
