#System-specific parameters and functions
import sys
#Low-level networking interface
import socket

#IP address to scan
destination = socket.gethostbyname(input("Insert IP address: "))

print("Scanning " + destination + ", please wait.")

try:
    #Scan ports range
    for port in range(100,150):
        #AF_INET = address family (host), SOCK_STREAM = TCP connection (ports)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #Default timeout between new socket connections
        socket.setdefaulttimeout(1)
        #Connect to a remote socket at address
        connection = s.connect_ex((destination, port))

        if(connection == 0):
            #Convert finded ports to string
            print("Port {} is open".format(port))

        #Close connection
        s.close()
except:
    print("Finishing...")
    sys.exit(0)


