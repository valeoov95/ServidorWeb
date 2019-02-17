#!/usr/bin/env python3

    import socket, sys

    host = "127.0.0.1"
    port = 8080
    filename = sys.argv[1]

    #Creacion del objeto socket (IPv4, TCP)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, e:
        print "Error creando el socket: %s" %e

    #Conectandolo hacia un host remoto
    try:
        s.connect((host, port))
    except socket.gaierror, e:
        print "Error conectando al servidor %s" %e
    try:
        s.sendall(filename)
    except socket.error, e:
        print "Error enviando datos: %s" %e
    while 1:
        try:
            buf = s.recv(2048)
        except socket.error, e:
            print "Error reciviendo datos: %s" %e
        if not len(buf):
            break
        sys.stdout.write(buf)
        