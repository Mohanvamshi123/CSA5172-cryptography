from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def generate_random_key():
    return get_random_bytes(16)

def ecb_encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

def ecb_decrypt(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

def cbc_encrypt(plaintext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

def cbc_decrypt(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

def cfb_encrypt(plaintext, key, iv):
    cipher = AES.new(key, AES.MODE_CFB, iv=iv)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

def cfb_decrypt(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CFB, iv=iv)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

def add_padding(data, block_size):
    padding_len = block_size - (len(data) % block_size)
    padding = b'\x80' + b'\x00' * (padding_len - 1)
    padded_data = data + padding
    return padded_data

def remove_padding(data):
    last_byte = data[-1]
    padding_len = data.count(last_byte)
    unpadded_data = data[:-padding_len]
    return unpadded_data

# ECB mode
def ecb_mode_demo():
    plaintext = b'This is a test message.'
    key = generate_random_key()

    padded_plaintext = add_padding(plaintext, 16)
    ciphertext = ecb_encrypt(padded_plaintext, key)
    decrypted_text = ecb_decrypt(ciphertext, key)

    print("ECB Mode:")
    print("Plaintext:", plaintext)
    print("Ciphertext:", ciphertext)
    print("Decrypted text:", decrypted_text)
    print()

# CBC mode
def cbc_mode_demo():
    plaintext = b'This is a test message.'
    key = generate_random_key()
    iv = generate_random_key()

    padded_plaintext = add_padding(plaintext, 16)
    ciphertext = cbc_encrypt(padded_plaintext, key, iv)
    decrypted_text = cbc_decrypt(ciphertext, key, iv)

    print("CBC Mode:")
    print("Plaintext:", plaintext)
    print("Ciphertext:", ciphertext)
    print("Decrypted text:", decrypted_text)
    print()

# CFB mode
def cfb_mode_demo():
    plaintext = b'This is a test message.'
    key = generate_random_key()
    iv = generate_random_key()

    ciphertext = cfb_encrypt(plaintext, key, iv)
    decrypted_text = cfb_decrypt(ciphertext, key, iv)

    print("CFB Mode:")
    print("Plaintext:", plaintext)
    print("Ciphertext:", ciphertext)
    print("Decrypted text:", decrypted_text)
    print()

# Run the demos
ecb_mode_demo()
cbc_mode_demo()
cfb_mode_demo()
