import os
import time

file_path = "./file.txt"

# Process A writes data to the file
def process_a_write(data):
    # Convert data to binary string
    binary_data = bin(data)[2:]

    # Write binary data to the file by appending '1' or '0' to the file content
    with open(file_path, 'w') as file:
        for bit in binary_data:
            if bit == '1':
                file.write('1\n')
            else:
                file.write('0\n')
            # Wait for a short duration to allow Process B to read
            time.sleep(0.1)

# Process B reads data from the file
def process_b_read():
    binary_data = ""
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip() == '1':
                binary_data += '1'
            else:
                binary_data += '0'
            # Wait for a short duration before reading next bit
            time.sleep(0.1)
    # Convert binary data to integer
    data = int(binary_data, 2)
    return data

# Example usage:
data_to_send = 10
process_a_write(data_to_send)
time.sleep(1)
received_data = process_b_read()
print("Received data:", received_data)
