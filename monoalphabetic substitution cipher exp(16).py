import string
from collections import Counter

# English letter frequency distribution
letter_freq = {
    'a': 0.08167, 'b': 0.01492, 'c': 0.02782, 'd': 0.04253,
    'e': 0.12702, 'f': 0.02228, 'g': 0.02015, 'h': 0.06094,
    'i': 0.06966, 'j': 0.00153, 'k': 0.00772, 'l': 0.04025,
    'm': 0.02406, 'n': 0.06749, 'o': 0.07507, 'p': 0.01929,
    'q': 0.00095, 'r': 0.05987, 's': 0.06327, 't': 0.09056,
    'u': 0.02758, 'v': 0.00978, 'w': 0.02360, 'x': 0.00150,
    'y': 0.01974, 'z': 0.00074
}

def letter_frequency_attack(ciphertext, num_top_plaintexts):
    # Remove all whitespace and convert to lowercase
    ciphertext = ''.join(ciphertext.split()).lower()
    # Count the occurrences of each letter in the ciphertext
    ciphertext_freq = Counter(ciphertext)
    # Calculate the total number of letters in the ciphertext
    total_letters = sum(ciphertext_freq.values())
    # Calculate the frequency of each letter in the ciphertext
    ciphertext_freq = {k: v/total_letters for k, v in ciphertext_freq.items()}
    # Calculate the letter frequency difference between the ciphertext and English language
    freq_diff = {k: abs(v - letter_freq[k]) for k, v in ciphertext_freq.items()}
    # Sort the letters by their frequency difference
    sorted_diff = sorted(freq_diff.items(), key=lambda x: x[1])
    # Generate all possible plaintexts
    possible_plaintexts = []
    for i in range(26):
        # Generate the substitution table
        substitution_table = {}
        for j in range(26):
            substitution_table[sorted_diff[j][0]] = string.ascii_lowercase[(j+i)%26]
        # Apply the substitution table to the ciphertext to generate the plaintext
        plaintext = ''.join([substitution_table[c] if c in substitution_table else c for c in ciphertext])
        possible_plaintexts.append(plaintext)
    # Return the top num_top_plaintexts plaintexts
    return possible_plaintexts[:num_top_plaintexts]
