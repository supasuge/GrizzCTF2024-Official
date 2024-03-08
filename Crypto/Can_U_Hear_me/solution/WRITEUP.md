# Can you hear me (Solution)

The encryption process works as follows:
- For each character in the message, take the corresponding character from the key (cycling back to the beginning if necessary), reverse it, and add its ASCII value to the message character's ASCII value.
- Take the result modulo 256 to get the encrypted character.
- Concatenate the encrypted characters and base64 encode the result to get the final ciphertext.

###### Source Code
```python
import base64
FLAG = open("flag.txt").readline().strip()

class ICantHearYou:
	def __init__(self, key):
		self.key = key
	
	def encrypt(self, message):
		encoded = ""
		for i in range(len(message)):
			key_c = self.key[i % len(self.key)][::-1]
			encoded_c = chr((ord(message[i]) + ord(key_c)) % 256)
			encoded += encoded_c
		return base64.b64encode(encoded.encode()).decode()
	
	def decrypt(self, message):
		decoded = ""
		message = base64.b64decode(message).decode()
		for i in range(len(message)):
			key_c = self.key[i % len(self.key)][::-1]
			decoded_c = chr((256 + ord(message[i]) - ord(key_c)) % 256)
			decoded += decoded_c
		return decoded

key = FLAG
dialog = ICantHearYou(key)
message = "Hi Alice, I'm Bob. I'm sending you a secret message. I hope you can decrypt it."
encrypted = dialog.encrypt(message)
with open("output.txt", "w") as f:
	f.write(encrypted)
	f.close()
```

###### Solution Source Code
```python
import base64
from Crypto.Util.number import *
st = 'wo/Dm8KJwrvDpsKswrfCq8KnYsK7V8OYU8Khw6PDimF/wq3CkMOOwozCo8OMw6vCq8Obw5fDocKawrzDg8K7wpvCo8KSwqPDkMKWw5HDmcOcU8OMw4nDnMOUw43Cl8OMwqtnwrvCicOiw6nCs8K5ZsO0wrHDp1DDjsKUw43ClMOMwpjDgsOWw6LDkcOgUMOQw7F1'
plaintext = "Hi Alice, I'm Bob. I'm sending you a secret message. I hope you can decrypt it."

def decrypt(message):
    flag = ""
    message = base64.b64decode(message).decode()
    for i in range(len(message)):
        for key_char in range(0, 256):
            if plaintext[i] == chr((256 + ord(message[i]) - key_char) % 256):
                flag += chr(key_char)
                break
    print(flag)
    return
print(decrypt(st))
```
### Explaination
At first glance, the cipher may seem secure... However it is vulnerable to a known plaintext attack. If we know part of the plaintext message, we can use that to then recover the key; or in this case, the flag.
- Here's how the solution works, as implemented in solution.py:
  - We have the encrypted message st and we know the corresponding plaintext - "Hi Alice, I'm Bob. I'm sending you a secret message. I hope you can decrypt it.".
  - In the decrypt function, we iterate through each character in the encrypted message:
  - For each possible key character `(0-255)`, we calculate what the decrypted character would be using the decryption formula: `chr((256 + ord(message[i]) - key_char) % 256)`.
    - If this matches the known plaintext character at that position, we've found the correct key character. We append it to the flag string and break out of the inner loop.
    - By the end of the iteration, we will have recovered the entire key, which is the flag.
  - We print out the flag!

So in essence, for each position, we brute force all possible key characters until we find the one that decrypts the ciphertext to the known plaintext at that position. We can do this because the encryption is a simple character-wise addition with the key, so knowing the plaintext and ciphertext directly gives us the key. This can also be seen in the `Vigenere! Oh my...` challenge where portions of the key could easily be infered by comparing the known plaintext with the ciphertext.

- This challenge demonstrates why it's crucial for encryption schems to be secure even when some plaintext-ciphertext pairs are known. Modern encryption algorithms like AES are designed to be resistant to known plaintext attacks. In this case, the flaw in the custom scheme allows us to easily recover the flag by leveraging our knowledge of the plaintext. Never ever use "Custom" encryption algorithm in production, it may be secure for you but in retrospect it will likely be broken instantaneously unless carefully designed by someone with extensive cryptographic knowledge.


