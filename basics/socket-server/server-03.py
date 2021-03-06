#/usr/bin/python
import socket
import sys

HOST = '' # Este servidor escuchara por todas las interfaces de red
PORT = 8888 # Un identificador de puerto cualquiera

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print 'Socket created'

try:
	s.bind((HOST, PORT)) # Esta funcion asocia un socket a un IP y un port
except socket.error, msg:
	print 'Bind failed. Error code: ' + str(msg[0]) + ' message ' + msg[1]
	sys.exit()

print 'Socket bind complete'

s.listen(10)
print 'Socket bind complete'

# Espera por una conexion - llamada bloqueante es decir que no se ejecutara
# la siguiente linea de codigo hasta tanto alguien no se conecte a este 
# IP y ese puerto
conn, addr = s.accept()

print "Conectado con " + addr[0] + ":" + str(addr[1])

# Ahora se le envia una informacion al cliente
data = conn.recv(1024)
conn.sendall("hola desde el server\n")

conn.close()
s.close()
