import network
import time

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('TP-LINK_716A90','58971703') # usurio e senha

while not wlan.isconnected():
    print(".",end="")
    time.sleep(0.1)

print("\nConectado")
print(wlan.ifconfig()) # imprimo o meu IP

def header(pag):
    resp = ('HTTP/1.1 200 OK\r\n'
            'Content-Type:text/html\r\n'
            'Connection: close\r\n'
            '\r\n'+pag+'\r\n\r\n')
    return resp

pagina = """
 <html><head></head>
 <body><h1>Ola</H1></body>
 </html>
"""


# criando um servidor local
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',80))

s.listen(5)

try:
    while True:
        conn, addr = s.accept()
        print(str(addr))
        conn.send(header(pagina).encode())
        conn.close()
    
  
except:
    print("erro")

s.close()

