
# encrypt data
def encrypt(input_file,encrypt_file,key):
    with open(input_file, 'rb') as f:
        data = f.read()
    #  # XOR encryption or decryption (same process for both)
    encrypt_array=bytearray()
    for byte in data:
        encrypt_array.append(byte ^ key)
    with open(encrypt_file, 'wb') as f:
        f.write(encrypt_array)

# decrypt data
def decrypt(encrypt_file,decrypt_file,key):

    #  # XOR decryption or encryption (same process for both)
    decrypt_array=bytearray()
    with open(encrypt_file, 'rb') as f:
        data=f.read()
    for byte in data:
        decrypt_array.append(byte ^ key)
    with open(decrypt_file, 'wb') as f:
        f.write(decrypt_array)


def main():
    input_file="input.txt"
    encrypt_file="encrypt.txt"
    decrypt_file="decrypt.txt"
    key=123
    # encryption by using xor alogrithm
    # encryption
    encrypt(input_file,encrypt_file,key)
    # decryption
    decrypt(encrypt_file,decrypt_file,key)

if __name__ == "__main__":
    main()