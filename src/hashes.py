import time
import hashlib

key = b"hello"
sha256key = hashlib.sha256(key).hexdigest()
print(hashlib.sha256(key).hexdigest())



def djb2(key):
    # Start from arbitrarily large prime number
    hash_value = 5381

    # bit-shift and sum the value for each character 

    for char in key:
        hash_value = ((hash_value << 5) + hash_value) + char
    return hash_value

print(djb2(key))
djb2key = djb2(key)


print(f"sha256 key: {int(sha256key) % 10}")
print(f"djb2 key: {djb2key % 10}")