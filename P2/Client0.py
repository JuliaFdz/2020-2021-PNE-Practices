import socket
import termcolor

class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def ping(self): # test if a website works
        print('Ok')
    def advanced_ping(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((self.ip, self.port)) # a tuple
            print('Server is up')
            s.close()
        except ConnectionRefusedError:
            print('Could not connect to the server')

    def __str__(self):
        # str representation of the class
        return 'Connection to SERVER at ' + self.ip + ' PORT: ' + str(self.port)


    def talk(self, msg):
        # -- Create the socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # establish the connection to the Server (IP, PORT)
        s.connect((self.ip, self.port))

        # Send data.
        #s.send(str.encode(msg))
        print('To server: ', msg)
        s.send(msg.encode())

        # Receive data
        response = s.recv(2048).decode("utf-8")

        # Close the socket
        s.close()

        # Return the response
        return 'From server ' + response
    @staticmethod
    def print_seq(list_sequences):
        for i in range(0, len(list_sequences)):
            text = 'Sequences'+ str(i) +':(length:' +  str(list_sequences[i].len()) + ')' + str(list_sequences[i])
            termcolor.cprint(text,'yellow')
