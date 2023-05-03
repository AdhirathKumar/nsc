def ceaserCipherEncryption(t, k):
    encryptedText = ""
    for i in t:
        if (i.isupper()):
            encryptedText += chr((ord(i) - 65 + k) % 26 + 65)
        elif (i.islower()):
            encryptedText += chr((ord(i) - 97 + k) % 26 + 97)
        else:
            encryptedText += " "
    return encryptedText


def ceaserCipherDecryption(t, k):
    decryptedText = ""
    for i in t:
        if (i.isupper()):
            decryptedText += chr((ord(i) - 65 - k) % 26 + 65)
        elif (i.islower()):
            decryptedText += chr((ord(i) - 97 - k) % 26 + 97)
        else:
            decryptedText += " "
    return decryptedText


text = "Welcome to MAVERICK"
key = 3
cipherText = ceaserCipherEncryption(text, key)
plainText = ceaserCipherDecryption(cipherText, key)
print(cipherText)
print(plainText)
