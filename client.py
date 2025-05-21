import socket
import serial
import time

serial_port_name = "/dev/ttyACM0"
serial_port = serial.Serial(serial_port_name, 9600)
time.sleep(2)

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('10.1.25.118', 8080))

    while True:
        data = serial_port.readline().decode('utf-8')
        print(data)
        client_socket.send(data.encode('utf-8'))
        if data.lower() == 'exit':
            print("Connection closed by the client.")
            break
            

    client_socket.close()

if __name__ == "__main__":
    start_client()

