# Uncomment this to pass the first stage
import socket
import threading

def on_new_client(conn):
    while True:
        data = conn.recv(1024)
        print("Received data", data)
        pong = "+PONG\r\n"
        conn.send(pong.encode())

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage

    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    while True:
        conn, addr = server_socket.accept()
        t = threading.Thread(target = on_new_client, args=(conn,)) # Start a new thread procee when a client connects.
        t.start()

if __name__ == "__main__":
    main()
