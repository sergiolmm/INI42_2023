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

# criando um cliente para a rede usando sockets
import socket

addr = socket.getaddrinfo('www.slmm.com.br',80)[0][-1]

s = socket.socket()
s.connect(addr)
s.send(b'GET / HTTP/1.0\r\nHost: www.slmm.com.br\r\n\r\n')
while True:
    data = s.recv(1024)
    if data:
        print(str(data, 'utf8'))
    else:
        break
s.close()







