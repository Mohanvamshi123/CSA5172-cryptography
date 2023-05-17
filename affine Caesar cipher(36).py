def affine_caesar_encrypt(plaintext, a, b):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                char_num = ord(char) - ord('A')
                encrypted_num = (a * char_num + b) % 26
                encrypted_char = chr(encrypted_num + ord('A'))
                ciphertext += encrypted_char
            else:
                char_num = ord(char) - ord('a')
                encrypted_num = (a * char_num + b) % 26
                encrypted_char = chr(encrypted_num + ord('a'))
                ciphertext += encrypted_char
        else:
            ciphertext += char
    return ciphertext

def affine_caesar_decrypt(ciphertext, a, b):
    plaintext = ""
    a_inverse = 0
    for i in range(26):
        if (a * i) % 26 == 1:
            a_inverse = i
            break
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                char_num = ord(char) - ord('A')
                decrypted_num = (a_inverse * (char_num - b)) % 26
                decrypted_char = chr(decrypted_num + ord('A'))
                plaintext += decrypted_char
            else:
                char_num = ord(char) - ord('a')
                decrypted_num = (a_inverse * (char_num - b)) % 26
                decrypted_char = chr(decrypted_num + ord('a'))
                plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext

# Example usage:
plaintext = "vamsi!"
a = 5
b = 8

ciphertext = affine_caesar_encrypt(plaintext, a, b)
print("Ciphertext:", ciphertext)

decrypted_text = affine_caesar_decrypt(ciphertext, a, b)
print("Decrypted text:", decrypted_text)
