import string
ALPHABET = list(string.ascii_uppercase)

def cipher(ciphertext,key):

    fullkey = ""
    while len(fullkey)<len(ciphertext):
        fullkey+=(key.translate(str.maketrans('', '', string.punctuation))).upper().replace(" ","")
    fullkey = fullkey[:len(ciphertext)]

    plaintext = ""
    j=0
    for i in range(len(ciphertext)):
        character = ciphertext[i]
        if character.upper() in ALPHABET:
            position = ALPHABET.index(character.upper())
            newpos = position+ALPHABET.index(fullkey[j])
            plaintext+=ALPHABET[newpos%26]
            j += 1
        else:
            plaintext+=character
    #print(plaintext)
    return plaintext

input_file = "Encrypted.txt"
output_file = "Decrypted.txt"
with open(input_file, 'r') as f:
      ciphertext = f.read()
      plaintext = cipher(ciphertext, "KEYWORD") #edit keyword if necessary
      with open(output_file, 'w') as out_f:
          out_f.write(plaintext)
print(plaintext)
print("decrypted")