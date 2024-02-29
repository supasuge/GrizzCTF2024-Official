# Vigenere?! Oh My...
*250 Points*
**Description:** You have been provided the partial plaintext + the ciphertext, can you solve for the missing plaintext given this information and retrieve the flag?

# Understanding the Vigenere Cipher
The vigenere cipher is a polyalphabetic cipher invented by French Cryptologist **Blaise de Vigenere** in the *16th century*. Encryption with vigenere goes as follows:
- Take the first letter of the message and the first letter of the key, add their value (letters have a value depending on there alphabetical index order beginning at A=0, B=1, ... Z=25). The result of the addition **modulo 26** give the enciphered letter as a result.
Ex:
- KEY = AZA | AZAAZAAZAAZAAZ

- PLAINTEXT = TESTTESTTESTES

- CIPHERTEXT= TDSTSESSTERTTD

- A[0] + T[20] % 26 = T[0](Plaintext unchanged) 20 % 26 -> 0

- Z[25] + E[4] % 26 = D[3]

- A[0] + S[19] % 26 = S[0] (Plaintext unchanged) 19 % 26 -> 0

... so on.

## Solution
To decrypt the ciphertext, there are many ways to go about doing so. The Kasiski Examination method of Vigenere Cryptanalysis is my preferred route as I find it is the most consistent, or at least gives enough information to enable you to be able to start brute forcing particular keyspaces more effectively. At which point further Cryptanalysis techniques can be applied.

### Understanding the Kasiski Examination
In polyalphabetic ciphers like vigenere, where the same plaintext letter can become different ciphertext letters, direct frequency analysis becomes significantly less effective. The Kasiski examination aims to determine the key length, bringing us much close to the solution once a known key length has been determined.

##### Kasiski Examination in detail
1. **Find repeating sequences**: This method looks for sequences of letters (usually 3 or more in length) that repeat within the ciphertext. The logic: when the same plaintext segment aligns with the same portion of the keyword, the resulting ciphertext seciont repeats as well.
2. **Analyzing Spacings**: Measure the distance (number of letters) betweeen the repeated sequences. If these distances are multiples of each other, there's a high chance that the common factor is the keyword length (or a multiple of it). It indicates how many letter have been encrypted before the shift pattern restarts due to the repeating keyword.
3. **GCD & Key Length**: Find the greatest common divisor (GCD) of the repeated sequence spacings. This GCD provides the most probable key length.
4. Once a key length is found, we can begin to refine our brute-force search for our target sequence; which in this case is the flag `GRIZZCTF`

###### Kasiski Exmaniation Python Implementation
```python
import string
from collections import defaultdict
from tabulate import tabulate
import itertools


class KasiskiExamination:
    def __init__(self, ciphertext):
        self.ciphertext = ciphertext

    def find_repeated_sequences(self):
        """Finds repeated sequences in the ciphertext and the distances between their occurrences."""
        spacings = defaultdict(list)
        for seq_len in range(3, 6):
            for i in range(len(self.ciphertext) - seq_len):
                seq = self.ciphertext[i:i + seq_len]
                for j in range(i + seq_len, len(self.ciphertext) - seq_len):
                    if self.ciphertext[j:j + seq_len] == seq:
                        spacings[seq].append(j - i)
        return spacings

    def find_key_length(self):
        """Finds the likely key length based on the spacings of repeated sequences."""
        spacings = self.find_repeated_sequences()
        distance_factors = defaultdict(int)
        for seq, spaces in spacings.items():
            for space in spaces:
                for factor in range(2, min(space, 10)):
                    if space % factor == 0:
                        distance_factors[factor] += 1

        likely_key_length = max(distance_factors, key=distance_factors.get)
        return likely_key_length

class VigenereBruteForce:
    def __init__(self, ciphertext, key_length):
        self.ciphertext = ciphertext
        self.key_length = key_length

    def vigenere_decrypt(self, ciphertext, key):
        """Decrypts a Vigenère cipher using the given key."""
        key_length = len(key)
        key_as_int = [ord(i) for i in key]
        ciphertext_int = [ord(i) for i in ciphertext]
        plaintext = ''
        for i in range(len(ciphertext_int)):
            value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
            plaintext += chr(value + 65)
        return plaintext

    def brute_force_vigenere(self, target_sequence):
        """Brute-force Vigenère cipher, looking for a specific sequence in the plaintext."""
        possible_keys = [''.join(k) for k in itertools.product(string.ascii_uppercase, repeat=self.key_length)]
        results = []

        for key in possible_keys:
            plaintext = self.vigenere_decrypt(self.ciphertext, key)
            if target_sequence in plaintext:
                results.append({"Key": key, "Plaintext": plaintext[:50]})  # Display the first 50 characters
                break  # Assuming we stop at the first successful decryption

        return results

# Using the classes to perform the Kasiski Examination and Brute Force the Vigenere Cipher
sample_ciphertext = 'GSKZAETGQUPWOVHLBIRJIHUJESGGSKZANYCGASUIMQVFIRJBZMABFCRTIRJBZMABFCRTCNEETGOALGSNGHBRPZ'
kasiski = KasiskiExamination(sample_ciphertext)
key_length = kasiski.find_key_length() # extract the key length (greatest common divisor of the spacings)
vigenere = VigenereBruteForce(sample_ciphertext, key_length)
print("key length found: ", key_length, "\nBrute forcing the keyspace now...\n")
# Brute-force the cipher looking for the first occurence of "GRIZZCTF" 
brute_force_results = vigenere.brute_force_vigenere("GRIZZCTF")
print(tabulate(brute_force_results, headers="keys"))
```

![alt text](image.png)

# Solution Method 2 (Manual)
Due to the partial plaintext given, it is relatively easy to manually reverse the encryption using the known values to find the repeating key sequence. This can be seen as follows below:

```
Ciphertext: 

GSKZAETGQUPWOVHLBIRJIHUJESGGSKZANYCGASUIMQVFIRJBZMABFCRTIRJBZMABFCRTCNEETGOALGSNGHBRPZ

Known plaintext:

xxxxxxxxxxxxxxxxxxxxxxxxxxxGRIZZLYBEARSILOVEGRIZZLYBEARSGRIZZLYBEARSANDCTFMAKESMEHAPPY

Key: [REDACTED]

[Vigenere Tableu for exemplary purposes]
ABCDEFGHIJKLMNOPQRSTUVWXYZ
BCDEFGHIJKLMNOPQRSTUVWXYZA
CDEFGHIJKLMNOPQRSTUVWXYZAB
DEFGHIJKLMNOPQRSTUVWXYZABC
EFGHIJKLMNOPQRSTUVWXYZABCD
FGHIJKLMNOPQRSTUVWXYZABCDE
GHIJKLMNOPQRSTUVWXYZABCDEF
HIJKLMNOPQRSTUVWXYZABCDEFG
IJKLMNOPQRSTUVWXYZABCDEFGH
JKLMNOPQRSTUVWXYZABCDEFGHI
KLMNOPQRSTUVWXYZABCDEFGHIJ
LMNOPQRSTUVWXYZABCDEFGHIJK
MNOPQRSTUVWXYZABCDEFGHIJKL
NOPQRSTUVWXYZABCDEFGHIJKLM
OPQRSTUVWXYZABCDEFGHIJKLMN
PQRSTUVWXYZABCDEFGHIJKLMNO
QRSTUVWXYZABCDEFGHIJKLMNOP
RSTUVWXYZABCDEFGHIJKLMNOPQ
STUVWXYZABCDEFGHIJKLMNOPQR
TUVWXYZABCDEFGHIJKLMNOPQRS
UVWXYZABCDEFGHIJKLMNOPQRST
VWXYZABCDEFGHIJKLMNOPQRSTU
WXYZABCDEFGHIJKLMNOPQRSTUV
XYZABCDEFGHIJKLMNOPQRSTUVW
YZABCDEFGHIJKLMNOPQRSTUVWX
ZABCDEFGHIJKLMNOPQRSTUVWXY
```

Because we know each flag stars wity **GRIZZCTF** let's simply input this above the ciphertext to see what we can find:
```
GSKZAETGQUPWOVHLBIRJIHUJESGGSKZANYCGASUIMQVFIRJBZMABFCRTIRJBZMABFCRTCNEETGOALGSNGHBRPZ
GRIZZCTFxxxxxxxxxxxxxxxxxxxGRIZZLYBEARSILOVEGRIZZLYBEARSGRIZZLYBEARSANDCTFMAKESMEHAPPY
```
Above, we can easily notice that the first letter is unchanged. This means the key is likely letter A for this position.
$G+A[0] mod 26$ -> 0 (Plaintext Unchanged in ciphertext)

A..A..A..A..A..A..A..A..A..A..A..A..A..A..A..A..A..A..A..A..A..A..A..A..A..A..A..A..A..A..A..A..A..A
**G**SK**Z**AE**T**GQ**U**PW**O**VH**L**BI**R**JI**H**UJ**E**SG**G**SK**Z**AN**Y**CG**A**SU**I**MQ**V**FI**R**JB**Z**MA**B**FC**R**TI**R**JB**Z**MA**B**FC**R**TC**N**EE**T**GO**A**LG**S**NG**H**BR**P**Z
**G**RI**Z**ZC**T**Fx**x**xx**x**xx**x**xx**x**xx**x**xx**x**xx**G**RI**Z**ZL**Y**BE**A**RS**I**LO**V**EG**R**IZ**Z**LY**B**EA**R**SG**R**IZ**Z**LY**B**EA**R**SA**N**DC**T**FM**A**KE**S**ME**H**AP**P**Y

Nice! So from the above example, the first letter of the key sequence is A. After analyzing the full ciphertext, this is a hit! Every third letter is unchanged and the key sequence is only 3 characters in length.



