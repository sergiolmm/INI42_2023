import network as net

redes_disp = net.WLAN(net.STA_IF)
redes_disp.active(True)

redes = redes_disp.scan()
print(redes)

arr = [12,13,14]
print(arr)
vet = (1,2,3,4)
print(vet)

for x in range(2,10):
    print(x)

for item in redes:
    print("rede : " + str(item))
    print("detalhe")
    for det in item:
        print(det)
    

