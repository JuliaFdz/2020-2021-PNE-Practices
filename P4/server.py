import socket
import termcolor
from pathlib import Path
from urllib.parse import urlparse, parse_qs


# -- Server network parameters
IP = "127.0.0.1"
PORT = 8080
HTML_ASSETS = "./HTML/"


def read_html_file(filename):
    content = Path(filename).read_text()
    # encoding="utf-8"
    return content
#leer archivo y poder coger la info, leer y crear -> funcion


def process_client(s):
    # -- Receive the request message
    req_raw = s.recv(2000)
    req = req_raw.decode()

    print("Message FROM CLIENT: ")

    # -- Split the request messages into lines
    lines = req.split('\n')

    # -- The request line is the first
    req_line = lines[0]
    request = req_line.split(" ")[1]
    o = urlparse(req_line.split(" ")[1])
    path_name = o.path
    arguments = parse_qs(o.query)
    print("Parameters ", arguments)
    print("Resource requested: ", path_name)

    print("Request line: ", end="")
    termcolor.cprint(req_line, "green")

    # -- Generate the response message
    # It has the following lines
    # Status line
    # header
    # blank line
    # Body (content to send)

    # This new contents are written in HTML language

    # -- Status line: We respond that everything is ok (200 code)
    status_line = "HTTP/1.1 200 OK\n"

    # -- Add the Content-Type header
    header = "Content-Type: text/HTML\n"

    if path_name == "/":
        body = read_html_file(HTML_ASSETS + "index.HTML") #url primer nombe -> path name
    elif "/info/" in path_name:
        # where is the letter? path_name.split("/")[-1] "A, C, T or G
        try:
            body = read_html_file(HTML_ASSETS + str(path_name.split("/")[-1]) + ".HTML")
            """if path_name == "/info/A":
                    body = read_html_file(HTML_ASSETS + "A.HTML")
                elif path_name == "/info/C":
                    body = read_html_file(HTML_ASSETS + "C.HTML")
                elif path_name == "/info/T":
                    body = read_html_file(HTML_ASSETS + "T.HTML")
                elif path_name == "/info/G":
                    body = read_html_file(HTML_ASSETS + "G.HTML")
                else:
                    body = read_html_file(HTML_ASSETS + "ERROR.HTML")"""
        except FileNotFoundError:
            body = read_html_file(HTML_ASSETS + "ERROR.HTML")
    else:
        body = read_html_file(HTML_ASSETS + "ERROR.HTML")

    # -- Add the Content-Length
    header += f"Content-Length: {len(body)}\n"

    # -- Build the message by joining together all the parts
    response_msg = status_line + header + "\n" + body
    cs.send(response_msg.encode())


# -------------- MAIN PROGRAM
# ------ Configure the server
# -- Listening socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Setup up the socket's IP and PORT
ls.bind((IP, PORT))

# -- Become a listening socket
ls.listen()

print("SEQ Server configured!")

# --- MAIN LOOP
while True:
    print("Waiting for clients....")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server Stopped!")
        ls.close()
        exit()
    else:

        # Service the client
        process_client(cs)

        # -- Close the socket
        cs.close()


