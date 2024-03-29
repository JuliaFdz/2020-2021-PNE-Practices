import socket

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
PORT = 8080
IP = "127.0.0.1"

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ls.bind((IP, PORT))
count_connections = 0
ls.listen()

print("The server is configured!")
client_address_list = []
while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")
    try:
        (cs, client_ip_port) = ls.accept()
        client_address_list.append(client_ip_port)
        count_connections += 1 # could be outside
        print('CONNECTION' + str(count_connections) + '.Client IP, PORT: ' + str(client_ip_port))

        # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()

    # -- Execute this part if there are no errors
    else:
        print("A client has connected to the server!")
        msg_raw = cs.recv(2048)
        msg = msg_raw.decode()
        print(f"Message received: {msg}")

        # -- Send a response message to the client
        response = 'ECHO' + msg
        cs.send(str(response).encode())
        # -- Close the data socket
        cs.close()
        if count_connections == 5:
            for i in range(0, len(client_address_list)):
                print('Client' + str(i) + ': Client IP, PORT: ' + str(client_address_list[i]))
            exit(0)
            # manually -1,  well 0, by an exception 1 --> errors meaning

