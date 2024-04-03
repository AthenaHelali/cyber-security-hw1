import os
import socket
import struct

ICMP_ECHO_REQUEST = 8
ICMP_CODE = socket.getprotobyname('icmp')

def checksum(data):
    if len(data) % 2 != 0:
        data += b'\x00'
    sum_ = 0
    for i in range(0, len(data), 2):
        sum_ += (data[i] << 8) + (data[i+1])
    sum_ = (sum_ >> 16) + (sum_ & 0xFFFF)
    sum_ += sum_ >> 16
    return (~sum_) & 0xFFFF

def create_packet(message):
    header = struct.pack('!BBHHH', ICMP_ECHO_REQUEST, 0, 0, os.getpid(), 1)
    data = bytes(message, 'utf-8')
    chksum = checksum(header + data)
    header = struct.pack('!BBHHH', ICMP_ECHO_REQUEST, 0, chksum, os.getpid(), 1)
    return header + data

def send_packet(dest_addr, message):
    try:
        raw_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, ICMP_CODE)
        packet = create_packet(message)
        raw_socket.sendto(packet, (dest_addr, 0))
        raw_socket.close()
        print(f"Sent message: {message} to {dest_addr}")
    except socket.error as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    destination = '127.0.0.1'
    message_to_send = "Secret message from sender"
    send_packet(destination, message_to_send)