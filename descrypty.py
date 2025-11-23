from cryptography.fernet import Fernet
import os

# Carregar chave de criptografia
def load_key():
    return open("secret.key", "rb").read()

# Descriptografar arquivo
def decrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as f:
        encrypted_data = f.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(file_path, "wb") as f:
        f.write(decrypted_data)

# Encontrar arquivos para descriptografar
def find_files_to_decrypt(directory):
    files_to_decrypt = []
    for root, _, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            if file != "descrypty.py" and not file.endswith(".key"):
                files_to_decrypt.append(path)
    return files_to_decrypt     

# Execução principal
def main():
    key = load_key()
    files = find_files_to_decrypt("test_files")
    for file_path in files:
        decrypt_file(file_path, key)
    print("All files have been decrypted!")

if __name__ == "__main__":
    main()  