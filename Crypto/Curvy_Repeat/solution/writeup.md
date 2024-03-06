# Curvy repeat (500 Points)
- *Difficulty*: Hard

This solution exploits the vulnerability of nonce reuse in ECDSA signatures. Given two signatures with the same nonce, one can recover the private key and decrypt an encrypted message.

### Mathematical Notation

- **Signatures**: Given two signatures $(r_1, s_1)$ and $(r_2, s_2)$ for messages $m_1$ and $m_2$ respectively, using the same nonce $k$, the ECDSA signature equations are:
  
  $$s_1 = k^{-1}(hash(m_1) + r \cdot priv) \mod n$$
  
  $$s_2 = k^{-1}(hash(m_2) + r \cdot priv) \mod n$$

  where $(hash(m))$ is the hash of message $m$, $(priv)$ is the private key, and $n$ is the order of the curve.

- **Nonce and Private Key Recovery**: By manipulating the above equations, one can solve for $k$ and $(priv)$. The key insight is that $k$ and $(priv)$ can be isolated due to the reuse of $k$ in both signatures.

### Steps

1. **Extract $r$ and $s$**: Extract the $r$ and $s$ components from the signatures.

2. **Solve for $k$**: Calculate $k$ using the difference between $s_1$ and $s_2$, and the hash differences of $m_1$ and $m_2$:

   $$k = (hash(m_1) - hash(m_2)) \cdot (s_1 - s_2)^{-1} \mod n$$

3. **Recover Private Key $(priv)$**: Once $k$ is known, $(priv)$ can be computed by rearranging the signature equations:

   $$priv = ((s \cdot k) - hash(m)) \cdot r^{-1} \mod n$$

4. **Decrypt the Flag**: With the private key recovered, the encrypted flag can be decrypted by XORing it with the private key:

   $$flag = ciphertext \oplus priv$$

### Conclusion

This challenge demonstrates a critical vulnerability in ECDSA: nonce reuse allows an attacker to recover the private key, undermining the security of the cryptographic scheme. It emphasizes the importance of using unique nonces for every signature in cryptographic protocols.
