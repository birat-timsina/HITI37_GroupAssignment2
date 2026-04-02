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
            encrypt_char = lower_encrypt(char,shift1,shift2) #encrypting the character using the lower_encrypt function
            encrypt_chars.append(encrypt_char)         #appending the encrypted character to the encrypt_chars list
            meta.append("L")           #appending "L" to the meta list to indicate that the character was a lowercase letter
        elif "A" <= char <="M":
            encrypt_char = upper_encrypt(char,shift1,shift2)      #encrypting the character using the upper_encrypt function
            encrypt_chars.append(encrypt_char) 
            meta.append("U")
        elif "n" <= char <="z":                            #checking if the character and encrypting it using the lower_encrypt function
            encrypt_char = lower_encrypt(char,shift1,shift2)
            encrypt_chars.append(encrypt_char)
            meta.append("L")
        elif "N" <= char <="Z":                #checking if the character and encrypting it using the upper_encrypt function
            encrypt_char = upper_encrypt(char,shift1,shift2)
            encrypt_chars.append(encrypt_char)
            meta.append("U")
        else:
            encrypt_chars.append(char)
            meta.append("0")

    return "".join(encrypt_chars), "".join(meta)

def decrypt_text(text, shift1, shift2, meta_text=None):         # Create list to collect decrypted characters.
	decrypted_chars = []                        
	for index, ch in enumerate(text):       # Loop with index so we can read matching metadata character.
		
		meta = meta_text[index] if meta_text and index < len(meta_text) else None   # Read metadata for this position if available, otherwise None.

		# If metadata says lowercase first half rule was used.
		if meta == "l":
			
			base = ord("a")         # Set lowercase ASCII base.
			shift = shift1 * shift2
			decrypted_chars.append(chr(base + (ord(ch) - base - shift) % 26))   # Reverse forward shift by subtracting it
		# If metadata says lowercase second half rule was used.
		elif meta == "r":
			base = ord("a")
			shift = shift1 + shift2 # For the second half, we used a different shift in encryption, so we need to reverse that specific shift.
			decrypted_chars.append(chr(base + (ord(ch) - base + shift) % 26))
		elif meta == "u":
			base = ord("A")
			shift = shift1 # For uppercase first half, we used the same shift as lowercase first half, so we reverse it the same way.
			decrypted_chars.append(chr(base + (ord(ch) - base + shift) % 26))
		elif meta == "v":
			base = ord("A")
			shift = shift2 ** 2 # For uppercase second half, we used a different shift in encryption, so we need to reverse that specific shift.
			decrypted_chars.append(chr(base + (ord(ch) - base - shift) % 26))
		elif "a" <= ch <= "z":
			decrypted_chars.append(lower_encrypt(ch, shift1, shift2))	# If no metadata and character is uppercase, use fallback brute force.
		elif "A" <= ch <= "Z":   # Decrypt uppercase by testing all candidates.
			decrypted_chars.append(upper_encrypt(ch, shift1, shift2))
		else:
			decrypted_chars.append(ch)	# Preserve spaces, punctuation, numbers, and newlines.

	# Join all decrypted characters into one string and return.
	return "".join(decrypted_chars)





