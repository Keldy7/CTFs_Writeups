text = ""
key = #à trouver

def crypt(text, key):
    crypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) - key
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            crypted_text += chr(shifted)
        else:
            crypted_text += char
    return crypted_text

crypted = crypt(text, key)
print(crypted)


"""
output = GAC{Bxa3q41_k0_o3q3}
"""
