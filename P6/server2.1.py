import http.server
import socketserver
import termcolor
import colorama
from urllib.parse import urlparse, parse_qs
import server_utils as su

LIST_SEQUENCES = ['ATTCTATGGATGACT', 'AACCTTTGAGATCAT', 'ATTGTTCTTCTTACT','AATACTTTTATCCCT', 'AAATTTCTCACTTTA']
LIST_GENES = {'ADA', 'FRAT1', 'FXN', 'RNU6_269P', 'U5'}
OPERATION_LIST = ["Info", "Complement", "Reverse"]
# Define the Server's port
PORT = 8080
HTML_ASSETS = "./HTML/info/"
HTML = "./HTML/"
BASES_INFORMATION = {
    "A": {"name": "ADENINE",
          "formula": "C5H5N5",
          "link": "https://en.wikipedia.org/wiki/Adenine",
          "color": "lightgreen"},
    "C": {"name": "CITOSINE",
          "formula": "C4H5N3O",
          "link": "https://en.wikipedia.org/wiki/Citosine",
          "color": "yellow"},
    "G": {"name": "GUANINE",
          "formula": "C5H5N5O",
          "link": "https://en.wikipedia.org/wiki/Guanine",
          "color": "lightblue"},
    "T": {"name": "TIMINE",
          "formula": "C5H5N2O2",
          "link": "https://en.wikipedia.org/wiki/Timine",
          "color": "pink"}
}
# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


#def read_html_file(filename):
#    return Path(filename).read_text()




# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        global contents
        colorama.init(strip="False")
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        termcolor.cprint(self.path, 'blue')

        o = urlparse(self.path)
        path_name = o.path
        arguments = parse_qs(o.query)
        print('Resource request: ', path_name)
        print('Parameters: ', arguments)

        # IN this simple server version:
        # We are NOT processing the client's request
        # It is a happy server: It always returns a message saying
        # that everything is ok
        # Message to send back to the client
        context = {}
        if path_name == "/":
            context['n_sequences'] = len(LIST_SEQUENCES)
            context['list_genes'] = LIST_GENES
            contents = su.read_template_html_file('./HTML/index.html').render(context=context)
        elif path_name == '/test':
            contents = su.read_template_html_file('./HTML/test.html').render()
        elif path_name == '/ping':
            contents = su.read_template_html_file('./HTML/ping.html').render()
        elif path_name == '/get':
            number_sequence = arguments['sequence'][0]
            contents = su.get(LIST_SEQUENCES, number_sequence)
        elif path_name == '/gene':
            gene = arguments['gene'][0]
            contents = su.gene(gene)
        elif path_name == "/operation":
            sequence = arguments["sequence"][0]
            operation = arguments["calculation"][0]
            if operation == "info":
                contents = su.info(sequence)
            elif operation == "comp":
                contents = su.comp(sequence)
            elif operation == "rev":
                contents = su.rev(sequence)
        else:
            contents = su.read_template_html_file('./HTML/error.html').render()

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!
        #length = len(contents.encode())
        # Define the content-type header:
        self.send_header('Content-Type', 'text/HTML')
        self.send_header('Content-Length', str(len(contents.encode())))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()
