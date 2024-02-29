def binary_to_ascii(binary_string):
    """
    Convert a binary string (with each 8-bit segment representing one ASCII character)
    back to the original ASCII string.
    """
    # Split the binary string into its 8-bit segments
    binary_segments = binary_string.split(' ')
    # Convert each binary segment to an ASCII character
    ascii_chars = [chr(int(segment, 2)) for segment in binary_segments]
    # Join the list of characters into a single string
    ascii_string = ''.join(ascii_chars)
    return ascii_string

# Example usage
binary_representation = "01000111 01110010 01101001 01111010 01111010 01000011 01010100 01000110 01111011 01100001 01110011 01100011 01101001 01101001 01011111 01110100 01101111 01011111 01100010 01100001 01110011 01100101 00110010 01111101"
ascii_string = binary_to_ascii(binary_representation)
print("ASCII representation of the binary:", ascii_string)
