import socket
import struct

ICMP_ECHO_REPLY = 0
ICMP_CODE = socket.getprotobyname('icmp')

def receive_packets():
    try:
        icmp_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, ICMP_CODE)
        while True:
            packet, addr = icmp_socket.recvfrom(1024)
            ip_header = packet[:20]
            icmp_header = packet[20:28]
            icmp_type, code, checksum, packet_id, seq = struct.unpack('!BBHHH', icmp_header)
            if icmp_type == ICMP_ECHO_REPLY:
                data = packet[28:]
                message = data.decode('utf-8')
                print(f"Received message: {message} from {addr[0]}")
    except socket.error as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    receive_packets()
