import random

def generate_key(length):
    key = []
    for _ in range(length):
        key.append(random.randint(0, 26))
    return key

def vigenere_encrypt(plaintext, key):
    ciphertext = ""
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                char_num = ord(char) - ord('A')
                shift = key[key_index]
                encrypted_num = (char_num + shift) % 26
                encrypted_char = chr(encrypted_num + ord('A'))
                ciphertext += encrypted_char
            else:
                char_num = ord(char) - ord('a')
                shift = key[key_index]
                encrypted_num = (char_num + shift) % 26
                encrypted_char = chr(encrypted_num + ord('a'))
                ciphertext += encrypted_char
            key_index = (key_index + 1) % len(key)
        else:
            ciphertext += char
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                char_num = ord(char) - ord('A')
                shift = key[key_index]
                decrypted_num = (char_num - shift) % 26
                decrypted_char = chr(decrypted_num + ord('A'))
                plaintext += decrypted_char
            else:
                char_num = ord(char) - ord('a')
                shift = key[key_index]
                decrypted_num = (char_num - shift) % 26
                decrypted_char = chr(decrypted_num + ord('a'))
                plaintext += decrypted_char
            key_index = (key_index + 1) % len(key)
        else:
            plaintext += char
    return plaintext

# Example usage:
plaintext = "Hello, World!"
key_length = len(plaintext)
key = generate_key(key_length)

ciphertext = vigenere_encrypt(plaintext, key)
print("Ciphertext:", ciphertext)

decrypted_text = vigenere_decrypt(ciphertext, key)
print("Decrypted text:", decrypted_text)
