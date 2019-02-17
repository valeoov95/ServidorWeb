#!/usr/bin/env python
# 
    import sys
    import cgi
    import socket
    import cgitb
    cgitb.enable()
# added code from mySocketsClient.py

    abs_dir = ''

def addOptions():
    parser = OptionParser()
    parser.add_option('-p', '--port', 
        dest='port', default='8080', 
        help='Define the port where the server will listen to conections.'
    )
    parser.add_option('-d', '--directory',
        dest='dir', default='.',
        help='Directory that will be used like root directory by the server.'
    )

    options, args = parser.parse_args()
    return options


def do_get():
    print(abs_dir, file_name)
    file_name = request.args.get('file')
    res = make_response(send_from_directory(abs_dir,file_name))
    res.headers['directory'] = abs_dir
    return 1

    def htmlTop():
     print("""Content-type:text/html\n\n
     <DOCTYPE html>
     <html lang="en">
       <head>
           <meta charset="utf-8" />
           <title> Servidor Web PBSI</title>
           <h1 align = "center">PSBI</h1>
           <h1 align = "center">Servidor Web</h1>
           <h2 align = "center">Realizado por</h2>
           <h3 align = "center">Flores Gómez Patricia</h3>
           <h3 align = "center">Ortiz Velarde Valeria</h3>
           </head>
           <body>""")
    def htmlTail():
     print("""<body/>
           </html> """   )

     #Según yo, getData y do_Get es lo mismo pero nos conviene do_Get para obtener el directorio 
     #def getData():
     #Se obtiene la información enviada por el usuario a través del navegadowr web 
     #formData = cgi.FieldStorage()
     #firstname = formData.getvalue("firstname")
     #return firstname

    def creSockettoServer():
# Create a TCP/IP socket
     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the port where the server is listening
# 
     server_address = ('localhost', 8080)
     sock.connect(server_address)
# Send data
     message = 'Este mensaje ha sido repetido'
     sock.sendall(message)
     return

#main program
    if __name__ == "__main__":

        try:

            htmlTop()
            print("Conectado (a)")
            abs_dir = do_Get()
            print(abs_dir)
            htmlTail()
            creSockettoServer()

        except:
            cgi.pri_exception()
