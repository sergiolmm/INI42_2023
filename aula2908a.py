# outra maneira de fazer import
from machine import Pin
help(Pin)
# set pino 2 para saida 
led = Pin(2, Pin.OUT)
# liga o pino 2 
led.value(1)

