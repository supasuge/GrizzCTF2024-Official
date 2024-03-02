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
