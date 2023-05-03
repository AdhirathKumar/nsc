import numpy as np


def getIndex(a):
    return (ord(a) - 65)


def hillCipherEncryption(t, k):
    encryptedText = ""
    l = len(k)
    pt = "".join(t.split())  # To remove the spaces in between them
    sp = [pt[i:i+l] for i in range(0, len(pt), l)]
    for i in sp:
        l = []
        for j in i:
            l.append(getIndex(j))
        res = np.matmul(l, k)
        for j in res:
            encryptedText += chr((j % 26) + 65)
    return encryptedText


text = "PAYMOREMONEY"
key = [[17, 17, 5], [21, 18, 21], [2, 2, 19]]
cipherText = hillCipherEncryption(text, key)

print(cipherText)
