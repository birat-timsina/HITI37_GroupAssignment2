
import os #importing os to check if file existence

BASE_DIR = os.path.dirname(__file__)

A = os.path.join(BASE_DIR, "raw_text.txt")
B = os.path.join(BASE_DIR, "encrypted", "encrypted_text.txt")
C = os.path.join(BASE_DIR, "decrypted", "decrypted_text.txt")
D = os.path.join(BASE_DIR, "metadata", "encryption_meta.txt")


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
        if "a" <= char <="m":                              # Lowercase first half (a-m): tag "L"
            encrypt_char = lower_encrypt(char,shift1,shift2)
            encrypt_chars.append(encrypt_char)
            meta.append("L")    # "L" = lowercase a-m half, base was ord("a")
        elif "n" <= char <="z":                            # Lowercase second half (n-z): tag "l"
            encrypt_char = lower_encrypt(char,shift1,shift2)
            encrypt_chars.append(encrypt_char)
            meta.append("l")    # "l" = lowercase n-z half, base was ord("n")
        elif "A" <= char <="M":                            # Uppercase first half (A-M): tag "U"
            encrypt_char = upper_encrypt(char,shift1,shift2)
            encrypt_chars.append(encrypt_char)
            meta.append("U")    # "U" = uppercase A-M half, base was ord("A")
        elif "N" <= char <="Z":                            # Uppercase second half (N-Z): tag "u"
            encrypt_char = upper_encrypt(char,shift1,shift2)
            encrypt_chars.append(encrypt_char)
            meta.append("u")    # "u" = uppercase N-Z half, base was ord("N")
        else:
            encrypt_chars.append(char)
            meta.append("0")    # "0" = not a letter, preserved as-is

    return "".join(encrypt_chars), "".join(meta)

def decrypt_text(text, shift1, shift2, meta_text=None):  # Create list to collect decrypted characters.
	decrypted_chars = []
	for index, ch in enumerate(text):       # Loop with index so we can read matching metadata character.

		meta = meta_text[index] if meta_text and index < len(meta_text) else None  # Read metadata for this position.
		shift = shift1 * shift2  # Same shift used in all encryption paths.

		if meta == "L":          # Original was in a-m, base was ord("a").
			base = ord("a")
			decrypted_chars.append(chr(base + (ord(ch) - base - shift) % 26))  # Reverse by subtracting shift.
		elif meta == "l":        # Original was in n-z, base was ord("n").
			base = ord("n")
			decrypted_chars.append(chr(base + (ord(ch) - base - shift) % 26))  # Reverse by subtracting shift.
		elif meta == "U":        # Original was in A-M, base was ord("A").
			base = ord("A")
			decrypted_chars.append(chr(base + (ord(ch) - base - shift) % 26))  # Reverse by subtracting shift.
		elif meta == "u":        # Original was in N-Z, base was ord("N").
			base = ord("N")
			decrypted_chars.append(chr(base + (ord(ch) - base - shift) % 26))  # Reverse by subtracting shift.
		else:
			decrypted_chars.append(ch)  # "0" or missing: preserve spaces, punctuation, numbers, newlines.

	# Join all decrypted characters into one string and return.
	return "".join(decrypted_chars)


def encryption_function(shift1, shift2):  # Try opening and reading the raw input file.
	try:
		
		with open(A, "r", encoding="utf-8") as source_file: # Open raw file in read mode with UTF-8 encoding.
			
			raw_text = source_file.read() # Read complete file text into memory.
	
	except FileNotFoundError:  # Handle missing file error safely.
		
		print("Error: raw_text.txt not found in the current folder.") # Print user-friendly error message.
		
		return False      # Return False to indicate step failed.

	
	encrypted_text, meta_text = encrypt_txt(raw_text, shift1, shift2) # Encrypt text and also generate metadata tags.

	
	with open(B, "w", encoding="utf-8") as encrypted_file:      # Open encrypted output file in write mode.
		
		encrypted_file.write(encrypted_text)      # Write encrypted text to file.

	
	with open(D, "w", encoding="utf-8") as meta_file:    # Open metadata file in write mode.
		
		meta_file.write(meta_text)     # Write metadata text to file.
	
	return True     # Return True to indicate step succeeded.

def decryption_function(shift1, shift2):
	"""Read encrypted_text.txt and write decrypted_text.txt."""
	try:
		with open(B, "r", encoding="utf-8") as encrypted_file:
			encrypted_text = encrypted_file.read()  # Read encrypted text.
	except FileNotFoundError:
		print("Error: encrypted_text.txt not found. Encryption may have failed.")
		return False

	meta_text = None  # Default when metadata file is missing.
	try:
		with open(D, "r", encoding="utf-8") as meta_file:
			meta_text = meta_file.read()  # Read metadata contents.
	except FileNotFoundError:
		meta_text = None

	decrypted_text = decrypt_text(encrypted_text, shift1, shift2, meta_text)

	with open(C, "w", encoding="utf-8") as decrypted_file:
		decrypted_file.write(decrypted_text)  # Write decrypted output.
	return True


def verification_function():
	"""Compare raw_text.txt and decrypted_text.txt and print result."""
	try:
		with open(A, "r", encoding="utf-8") as source_file:
			original_text = source_file.read()  # Read original text.
		with open(C, "r", encoding="utf-8") as decrypted_file:
			decrypted_text = decrypted_file.read()  # Read decrypted text.
	except FileNotFoundError:
		print("Verification failed: required files are missing.")
		return

	if original_text == decrypted_text:
		print("Decryption successful: decrypted text matches the original.")
	else:
		print("Decryption failed: decrypted text does not match the original.")


def main():
	"""Run the full assignment workflow."""
	os.makedirs(BASE_DIR + "/encrypted", exist_ok=True)  # Ensure output dirs exist.
	os.makedirs(BASE_DIR + "/decrypted", exist_ok=True)
	os.makedirs(BASE_DIR + "/metadata", exist_ok=True)

	try:
		shift1 = int(input("Enter shift1: "))  # Read shift1 from input.
		shift2 = int(input("Enter shift2: "))  # Read shift2 from input.
	except ValueError:
		print("Invalid input. Please enter integer values for shift1 and shift2.")
		return

	if not encryption_function(shift1, shift2):
		return

	if not decryption_function(shift1, shift2):
		return

	verification_function()


if __name__ == "__main__":
	main()  # Start program from main.





