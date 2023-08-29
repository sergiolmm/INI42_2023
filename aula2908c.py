# conectando ao celular via wifi
import network
import time


wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('Unicamp-Visitante','') # usurio e senha

while not wlan.isconnected():
    print(".",end="")
    time.sleep(0.1)

print("\nConectado")
print(wlan.ifconfig()) # imprimo o meu IP




