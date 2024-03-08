import streamlit as st
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

# Function to encrypt messages using the provided public key
def encrypt_message(public_key, message):
    try:
        key_size = public_key.size_in_bytes()
        max_chunk_size = key_size - 42
        chunks = [message[i:i+max_chunk_size] for i in range(0, len(message), max_chunk_size)]
        encrypted_chunks = []
        cipher = PKCS1_OAEP.new(public_key)
        for chunk in chunks:
            encrypted_chunk = cipher.encrypt(chunk.encode())
            encrypted_chunks.append(base64.b64encode(encrypted_chunk).decode())
        delimiter = '|'
        encrypted_message = delimiter.join(encrypted_chunks)
        return True, encrypted_message
    except Exception as e:
        return False, str(e)

# Function to decrypt messages using the provided private key
def decrypt_message(private_key, encrypted_message):
    try:
        cipher = PKCS1_OAEP.new(private_key)
        encrypted_chunks = encrypted_message.split('|')
        decrypted_chunks = []
        for chunk in encrypted_chunks:
            decrypted_chunk = cipher.decrypt(base64.b64decode(chunk))
            decrypted_chunks.append(decrypted_chunk)
        decrypted_message = b''.join(decrypted_chunks)
        return True, decrypted_message.decode()
    except Exception as e:
        return False, str(e)

# Function to generate RSA keys
def generate_rsa_keys(key_size=2048):
    try:
        key = RSA.generate(key_size)
        private_key = key.export_key()
        public_key = key.publickey().export_key()
        return True, private_key, public_key
    except Exception as e:
        return False, str(e), None

# Helper function for message input
def get_message_from_user(input_type, file_uploader_key, text_area_key):
    if input_type == "Type":
        message = st.text_area("Type your message here:", key=text_area_key)
        return message.encode('utf-8') if message else None
    elif input_type == "Upload":
        uploaded_file = st.file_uploader("Or upload a .txt file:", type=['txt'], key=file_uploader_key)
        if uploaded_file is not None:
            return uploaded_file.getvalue()
    return None

# Streamlit UI
st.sidebar.title("Navigation")
app_mode = st.sidebar.selectbox("Choose the app mode", ["Home", "Generate Keys", "Encrypt Message", "Decrypt Message"])

if app_mode == "Home":
    st.title('RSA Encryption/Decryption App')
    st.write("Welcome to the RSA Encryption/Decryption App. Please select an option from the navigation bar to start.")

elif app_mode == "Generate Keys":
    st.title('Generate RSA Keys')
    key_size_option = st.selectbox("Select Key Size", [2048, 3072, 4096], index=0)
    key_strength_info = {
        2048: "Sufficient for most purposes",
        3072: "Higher security, slower performance",
        4096: "Highest security, significantly slower performance"
    }
    st.write(f"Key Strength: {key_strength_info[key_size_option]}")
    if st.button("Generate Keys"):
        with st.spinner('Generating RSA Keys...'):
            success, private_key, public_key = generate_rsa_keys(key_size=key_size_option)
        if success:
            st.success("Keys generated successfully!")
            st.text_area("Public Key", public_key.decode('utf-8'), height=250)
            st.download_button("Download Public Key", public_key, "public_key.pem", "text/plain")
            st.text_area("Private Key", private_key.decode('utf-8'), height=250)
            st.download_button("Download Private Key", private_key, "private_key.pem", "text/plain")
            st.warning("Remember to store your private key in a secure location. It is crucial for decrypting your messages and must be kept confidential.")
        else:
            st.error(f"Failed to generate keys: {private_key}")  # private_key holds the error message in this case

elif app_mode == "Encrypt Message":
    st.title('Encrypt Message')
    pub_key = st.file_uploader("Upload Public Key", type=['pem'])
    if pub_key:
        public_key = RSA.import_key(pub_key.getvalue())
        input_type = st.radio("How would you like to input your message?", ("Type", "Upload"), key="encrypt_input_type")
        message_to_encrypt = get_message_from_user(input_type, "encrypt_file_uploader", "encrypt_text_area")
        if message_to_encrypt and st.button("Encrypt"):
            success, encrypted_message = encrypt_message(public_key, message_to_encrypt.decode('utf-8'))
            if success:
                st.text_area("Encrypted Message", encrypted_message, height=100)
                st.download_button("Download Encrypted Message", encrypted_message, "encrypted_message.txt", "text/plain")
                st.success("Message encrypted successfully!")
            else:
                st.error(f"Encryption failed: {encrypted_message}")  # encrypted_message holds the error message in this case

elif app_mode == "Decrypt Message":
    st.title('Decrypt Message')
    priv_key = st.file_uploader("Upload Private Key", type=['pem'])
    if priv_key:
        private_key = RSA.import_key(priv_key.getvalue())
        input_type = st.radio("How would you like to input your encrypted message?", ("Type", "Upload"), key="decrypt_input_type")
        encrypted_msg_to_decrypt = get_message_from_user(input_type, "decrypt_file_uploader", "decrypt_text_area")
        if encrypted_msg_to_decrypt and st.button("Decrypt"):
            success, decrypted_message = decrypt_message(private_key, encrypted_msg_to_decrypt.decode('utf-8'))
            if success:
                st.text_area("Decrypted Message", decrypted_message, height=100)
                st.download_button("Download Decrypted Message", decrypted_message, "decrypted_message.txt", "text/plain")
                st.success("Message decrypted successfully!")
            else:
                st.error(f"Decryption failed: {decrypted_message}")  # decrypted_message holds the error message in this case
