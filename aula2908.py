# exemplos de como importa um modulp (lib)
import machine
import time

# mostra o conteudo de um modulo
help(machine)

led = machine.Pin(2, machine.Pin.OUT)

led.value(1) 
time.sleep(1.0)
led.value(0)