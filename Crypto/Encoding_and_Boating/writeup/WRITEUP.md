# Encoding and Boating
**Description:** I made a *highly* original decoder, can you decode the string provided below to get the flag?

`KIZUU4DFNZYEIVSFLI3WI3KWPFSVMOJRMJWWY6DEK5LGMWSXGVVGEMSSOBRG2ZD2LAZGQMLBIQ4TS===`

- Output from [solve.py](solve.py)
![alt text](image.png)

```python
import json
from base64 import b64encode as honestlynoideawhatimdoing
from base64 import b32encode as geronimo
file_path = '[REDACTED--Unimportant]'
with open(file_path) as f:
    data=json.load(f)
    flag = data['crypto']['flag2']
stringjuan = geronimo(honestlynoideawhatimdoing(flag.encode()))
with open('ciphertext.txt', 'w') as f:
    f.write(stringjuan.decode())
```
To reverse this, simply base32 decode the given string, then base64 decode the output from the previous base32 encoding. This will result in the plaintext flag.
