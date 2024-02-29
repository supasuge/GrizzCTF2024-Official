def hex_to_ascii(hex_string):
    """
    Convert a hex string to its ASCII representation.
    """
    # Remove the '0x' prefix if present
    hex_string = hex_string[2:] if hex_string.startswith('0x') else hex_string
    # Convert each pair of hex digits to the corresponding ASCII character
    ascii_string = ''.join(chr(int(hex_string[i:i+2], 16)) for i in range(0, len(hex_string), 2))
    return ascii_string

# Given values
flag_hex = "0x4772697a7a4354467b61736369695f746f5f62617365325f775f74773172747c"
key = 0x10001

# XOR the flag with the key
xor_result = hex(int(flag_hex, 16) ^ key)

# Convert the XOR result to ASCII
ascii_result = hex_to_ascii(xor_result)

print("ASCII representation of the XOR result:", ascii_result)
