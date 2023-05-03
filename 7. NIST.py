from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes

# Key generation
private_key = dsa.generate_private_key(key_size=1024)
public_key = private_key.public_key()

# Message hashing
message = b"Hello, world!"
digest = hashes.SHA256()
hasher = hashes.Hash(digest)
hasher.update(message)
hashed_message = hasher.finalize()

# Signature generation
signature = private_key.sign(hashed_message, algorithm=hashes.SHA256())

# Signature verification
try:
    public_key.verify(signature, hashed_message, algorithm=hashes.SHA256())
    print("Signature is valid!")
except:
    print("Invalid signature.")
