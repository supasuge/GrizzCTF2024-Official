# Can you XOR or NOT
- Category: Cryptography
- Difficulty: Beginner/medium

**Description:** A mysterious message has been intercepted, seemingly protected by a simple cipher. It appears to be XOR encryption, although something is afoot. Given the key used, can you decrypt the message?

##### Source Code (`solve.py`)
```python
from pwn import xor

ciphertext = "20000000002f2d19190b501116380a590825014100533a134a2c5f5d5107"
key = b"grizzly_bears"


# Perform XOR decryption
flag_bytes = xor(bytes.fromhex(ciphertext), key)

print(flag_bytes.decode("utf-8"))

```
1. `pip install pwntools`
2. `python ../src/solve.py`
```
![alt text](.\image.png)


