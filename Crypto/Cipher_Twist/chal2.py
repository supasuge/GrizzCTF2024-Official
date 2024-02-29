from pwn import xor

def ascii_to_binary(input_string):
    # Convert each character in the input string to its binary representation
    binary_strings = [format(ord(char), '08b') for char in input_string]
    # Join the list of binary strings into a single string
    binary_representation = ''.join(binary_strings)  # Remove spaces for continuous binary data
    return binary_representation

def binary_to_int(binary_string):
    # Convert binary string to integer
    return int(binary_string, 2)

def int_to_hex(integer_value):
    # Convert integer to hexadecimal string
    return hex(integer_value)

# Example usage
flag = "GrizzCTF{ascii_to_base2_w_tw1st}"
KEY = 0x10001

# Convert flag to binary and then to integer
binary_flag = ascii_to_binary(flag)
flag_int = binary_to_int(binary_flag)

# XOR the integer representation of the flag with KEY
xor_result = flag_int ^ KEY  # Using Python's built-in XOR operation

# Convert the result to hexadecimal
hex_result = int_to_hex(xor_result)

print("Hex representation of the XORed flag:", hex_result)
print("Flag Int: ", flag_int)
# Optionally, write the hex result to a file
with open("challenge.txt", "w") as f:
    f.write(f"flag = {hex_result}\n")
