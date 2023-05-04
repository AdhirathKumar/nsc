from Cryptodome.Signature import DSS
from Cryptodome.PublicKey import DSA
from Cryptodome.Hash import SHA256

# Generate a DSA key pair
key = DSA.generate(2048)

# Compute the SHA-256 hash of the message
message = b"Hello, World!"
hash_obj = SHA256.new(message)
hash_value = hash_obj.digest()

# Use the private key to generate a digital signature
signer = DSS.new(key, 'fips-186-3')
signature = signer.sign(hash_obj)

print("Digital signature:", signature.hex())
