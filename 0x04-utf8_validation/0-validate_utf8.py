#!/usr/bin/python3

def validUTF8(data):
    # Initialize the number of bytes in the current character
    num_bytes = 0

    # Iterate over the data set
    for byte in data:
        # Check if the byte is a valid start byte
        if not (byte & 0b11110000 == 0b11000000):
            return False

        # Check if the byte is the start of a multi-byte character
        if num_bytes == 0:
            # Check if the byte is the start of a 2-byte character
            if byte & 0b11100000 == 0b11000000:
                num_bytes = 2
            # Check if the byte is the start of a 3-byte character
            elif byte & 0b11110000 == 0b11100000:
                num_bytes = 3
            # Check if the byte is the start of a 4-byte character
            elif byte & 0b11111000 == 0b11110000:
                num_bytes = 4
            else:
                return False

        # Check if the byte is a continuation byte
        elif num_bytes > 0:
            # Check if the byte is a valid continuation byte
            if not (byte & 0b11000000 == 0b10000000):
                return False
            num_bytes -= 1

        # Check if the byte is the end of a character
        else:
            return False

    # Check if the number of bytes in the current character is valid
    if num_bytes > 0:
        return False

    # The data set is a valid UTF-8 encoding
    return True
