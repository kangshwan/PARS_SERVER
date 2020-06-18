import socket
import threading,time

port = 60000

def handle_client(client_socket, addr):
    recvData = client_socket.recv(1024)
    print(recvData.decode('utf-8'))
    time.sleep(2)
    client_socket.close()

def accept_func():
    global server_socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('', port))
    server_socket.listen(10)
    while 1:
        try:
            client_socket, addr = server_socket.accept()
        except KeyboardInterrupt:
            server_socket.close()
            print("Keyboard interrupt")
        t = threading.Thread(target=handle_client, args=(client_socket, addr))
        t.daemon = True
        t.start()

if __name__ == '__main__':
    accept_func()