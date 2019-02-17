#!/usr/bin/python
    import socket, sys
    host="127.0.0.1"
    port=8080
    message=sys.argv[1]
    try:
        s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error, e:
        print "Error creando el socket: %s:" %e
    try:
        s.sendto(message,(host,port))
    except socket.error, e:
        print "Error enviando datos: %s" %e
    s.settimeout(5)
    while 1:
        try:
            message, address=s.recvfrom(2048)
        except socket.timeout:
            print "Cerrado por inactividad"
            sys.exit(1)
        except socket.error, e:
            print "Error recibiendo datos: %s" %e
        if not len(message):
            break
        sys.stdout.write(message+"\n")