#File encyption and decryption with verification

import os #importing os to check if file existence

def lower_encrypt(char,shift1,shift2):   #function to encrypt lowercase characters
    if "a" <= char <="m":                #checking if the character is in the first half of the alphabet
        shift = shift1 * shift2          #calculating the total shift by multiplying the two shift values
        base = ord("a")                  #getting the ASCII value of 'a' to use as a base for the shift
        return chr((ord(char) - base + shift) % 26 + base) #shifting the character by the calculated shift and wrapping around using modulo 26, then converting back to a character
    

    if "n" <= char <="z":     #checking if the character is in the second half of the alphabet
        shift = shift1 * shift2
        base = ord("n")                  #getting the ASCII value of 'n' to use as a base for the shift
        return chr((ord(char) - base + shift) % 26 + base)
    
    return char


def upper_encrypt(char,shift1,shift2):  #function to encrypt uppercase characters
    if "A" <= char <="M":
        shift = shift1 * shift2
        base = ord("A")           #getting the ASCII value of 'A' to use as a base for the shift
        return chr((ord(char) - base + shift) % 26 + base)
    

    if "N" <= char <="Z":
        shift = shift1 * shift2
        base = ord("N")                  #getting the ASCII value of 'N' to use as a base for the shift
        return chr((ord(char) - base + shift) % 26 + base)
    
    return char

def encrypt_txt(text,shift1,shift2):   #function to encrypt the entire text using the lower_encrypt and upper_encrypt functions.
    encrypt_chars = []
    meta = []
    
    for char in text:
        if "a" <= char <="m":
            encrypt_char = lower_encrypt(char,shift1,shift2)
            encrypt_chars.append(encrypt_char)
            meta.append("L")
        elif "A" <= char <="M":
            encrypt_char = upper_encrypt(char,shift1,shift2)
            encrypt_chars.append(encrypt_char)
            meta.append("U")
        elif "n" <= char <="z":
            encrypt_char = lower_encrypt(char,shift1,shift2)
            encrypt_chars.append(encrypt_char)
            meta.append("L")
        elif "N" <= char <="Z":
            encrypt_char = upper_encrypt(char,shift1,shift2)
            encrypt_chars.append(encrypt_char)
            meta.append("U")
        else:
            encrypt_chars.append(char)
            meta.append("0")

    return "".join(encrypt_chars), "".join(meta)
#File encyption and decryption with verification

import os #importing os to check if file existence

def lower_encrypt(char,shift1,shift2):   #function to encrypt lowercase characters
    if "a" <= char <="m":                #checking if the character is in the first half of the alphabet
        shift = shift1 * shift2          #calculating the total shift by multiplying the two shift values
        base = ord("a")                  #getting the ASCII value of 'a' to use as a base for the shift
        return chr((ord(char) - base + shift) % 26 + base) #shifting the character by the calculated shift and wrapping around using modulo 26, then converting back to a character
    

    if "n" <= char <="z":     #checking if the character is in the second half of the alphabet
        shift = shift1 * shift2
        base = ord("n")                  #getting the ASCII value of 'n' to use as a base for the shift
        return chr((ord(char) - base + shift) % 26 + base)
    
    return char


def upper_encrypt(char,shift1,shift2):  #function to encrypt uppercase characters
    if "A" <= char <="M":
        shift = shift1 * shift2
        base = ord("A")           #getting the ASCII value of 'A' to use as a base for the shift
        return chr((ord(char) - base + shift) % 26 + base)
    

    if "N" <= char <="Z":
        shift = shift1 * shift2
        base = ord("N")                  #getting the ASCII value of 'N' to use as a base for the shift
        return chr((ord(char) - base + shift) % 26 + base)
    
    return char

def encrypt_txt(text,shift1,shift2):   #function to encrypt the entire text using the lower_encrypt and upper_encrypt functions.
    encrypt_chars = []
    meta = []
    
    for char in text:
        if "a" <= char <="m":
            encrypt_char = lower_encrypt(char,shift1,shift2)
            encrypt_chars.append(encrypt_char)
            meta.append("L")
        elif "A" <= char <="M":
            encrypt_char = upper_encrypt(char,shift1,shift2)
            encrypt_chars.append(encrypt_char)
            meta.append("U")
        elif "n" <= char <="z":
            encrypt_char = lower_encrypt(char,shift1,shift2)
            encrypt_chars.append(encrypt_char)
            meta.append("L")
        elif "N" <= char <="Z":
            encrypt_char = upper_encrypt(char,shift1,shift2)
            encrypt_chars.append(encrypt_char)
            meta.append("U")
        else:
            encrypt_chars.append(char)
            meta.append("0")

    return "".join(encrypt_chars), "".join(meta)


