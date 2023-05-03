def gcd(a,b):
    if(b == 0):
        return abs(a)
    else:
        return gcd(b, a % b)

p = int(input('Enter first large Primary Number:'))
q = int(input('Enter second large Primary Number:'))
n = p*q
phi = (p-1)*(q-1)

for e in range(2,phi):
  if(gcd(e,phi)==1):
    break

d = pow(e, -1, phi)

print('Public Key Pair: {',e,',',n,'}')
print('Private Key Pair: {',d,',',n,'}')

m = int(input("Enter the message to be delivered: "))

encryptedText = pow(m,e,n)
decryptedText = pow(encryptedText,d,n)

print(encryptedText,decryptedText)
