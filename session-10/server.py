import socket

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Configure the Server's IP and PORT
PORT = 8080
IP = "127.0.0.1"

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))
count_connections = 0
# -- Step 3: Configure the socket for listening
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

        # -- Read the message from the client
        # -- The received message is in raw bytes
        msg_raw = cs.recv(2048)

        # -- We decode it for converting it
        # -- into a human-redeable string
        msg = msg_raw.decode()

        # -- Print the received message
        print(f"Message received: {msg}")

        # -- Send a response message to the client
        #response = "HELLO. I am the Happy Server :-)\n"
        # everything is traduced to a str
        try:
            response = int(msg) ** int(msg)
            print('Response', response)

            # -- The message has to be encoded into bytes
            #cs.send(response.encode())
            cs.send(str(response).encode()) #encode depends on a str
        except ValueError:
            cs.send('we need a number'.encode())


        # -- Close the data socket
        cs.close()
        if count_connections == 5:
            for i in range(0, len(client_address_list)):
                print('Client' + str(i) + ': Client IP, PORT: ' + str(client_address_list[i]))
            exit(0)
            # manually -1,  well 0, by an exception 1 --> errors meaning





#echo 2 | nc -w 1 127.0.0.1 8080