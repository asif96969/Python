alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
declaration = input("type 'encode' to encrypt and type 'decode' to decrypt: \n")
text = input("Take the message:")
shift = int(input("take a number that you want to shift:"))

def plain_chaiper(plain_text, shift_amount):
    chiper = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_alpha = alphabet[new_position]
        chiper += new_alpha
    return chiper

def chiper_plain(chipered_text, shifted_amount):
    plain = ""
    for letter in chipered_text:
        position = alphabet.index(letter)
        new_position = position - shifted_amount
        new_alpha = alphabet[new_position]
        plain += new_alpha
    return plain

chiper_text = plain_chaiper(text, shift)
print(f"The text is encryptet {chiper_text}")
plain_text = chiper_plain(chiper_text, shift)
print(f"The text is encryptet {plain_text}")






