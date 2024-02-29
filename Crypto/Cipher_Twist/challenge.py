def ascii_to_binary(input_string):
    # Convert each character in the input string to its binary representation
    binary_strings = [format(ord(char), '08b') for char in input_string]
    # Join the list of binary strings into a single string
    binary_representation = ' '.join(binary_strings)
    return binary_representation
from pwn import xor
# Example usage
flag = "GrizzCTF{ascii_to_base2_w_tw1st}"
KEY = 0x10001
binary_flag = ascii_to_binary(flag)
print("Binary representation of the flag:", binary_flag)
with open("challenge.txt", "w") as f:
    f.write(f"flag = {binary_flag}")
    f.close()