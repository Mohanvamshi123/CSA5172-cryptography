import string
import random

# Function to generate a random key stream of the specified length
def generate_key(length):
    return [random.randint(0, 26) for _ in range(length)]

# Function to encrypt the plaintext using the key stream
def encrypt(plaintext, key):
    ciphertext = ""
    for i, c in enumerate(plaintext):
        # Convert the character to a number between 0 and 25
        num = string.ascii_lowercase.index(c.lower())
        # Encrypt the number using the key stream
        encrypted_num = (num + key[i % len(key)]) % 26
        # Convert the encrypted number back to a character and append it to the ciphertext
        ciphertext += string.ascii_lowercase[encrypted_num]
    return ciphertext

# Encrypt the plaintext "send more money" with the key stream [9, 0, 1, 7, 23, 15, 21, 14, 11, 11, 2, 8, 9]
plaintext = "send more money"
key_stream = [9, 0, 1, 7, 23, 15, 21, 14, 11, 11, 2, 8, 9]
ciphertext = encrypt(plaintext, key_stream)
print("Ciphertext:", ciphertext)

# Function to decrypt the ciphertext using a given key
def decrypt(ciphertext, key):
    plaintext = ""
    for i, c in enumerate(ciphertext):
        # Convert the character to a number between 0 and 25
        num = string.ascii_lowercase.index(c.lower())
        # Decrypt the number using the key
        decrypted_num = (num - key[i % len(key)]) % 26
        # Convert the decrypted number back to a character and append it to the plaintext
        plaintext += string.ascii_lowercase[decrypted_num]
    return plaintext

# Decrypt the ciphertext to get the key
target_plaintext = "cash not needed"
for i in range(len(ciphertext) - len(target_plaintext)):
    # Extract a substring of the ciphertext with the same length as the target plaintext
    substring = ciphertext[i:i+len(target_plaintext)]
    # Generate a candidate key by subtracting the corresponding ciphertext and plaintext characters
    candidate_key = [(string.ascii_lowercase.index(substring[j]) - string.ascii_lowercase.index(target_plaintext[j])) % 26 for j in range(len(target_plaintext))]
    # Decrypt the ciphertext using the candidate key
    candidate_plaintext = decrypt(ciphertext, candidate_key)
    # Check if the candidate plaintext is equal to the target plaintext
    if candidate_plaintext == target_plaintext:
        print("Key:", candidate_key)
        break
