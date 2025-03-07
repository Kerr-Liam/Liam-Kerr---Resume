from machine import Pin
import time

Game = True

reset = Pin(15, Pin.IN, Pin.PULL_UP)
Game_led = Pin(14, Pin.OUT)

button_1 = Pin(18, Pin.IN, Pin.PULL_UP)
button_1_led = Pin(19,Pin.OUT)
button_1_push = 0

button_2 = Pin(20, Pin.IN, Pin.PULL_UP)
button_2_led = Pin(21, Pin.OUT)
button_2_push = 0

button_3 = Pin(16, Pin.IN, Pin.PULL_UP)
button_3_led = Pin(17, Pin.OUT)
button_3_push = 0

button_4 = Pin(12, Pin.IN, Pin.PULL_UP)
button_4_led = Pin(13, Pin.OUT)
button_4_push = 0

buzzer = Pin(2, Pin.OUT)

button_1_led.off()
button_2_led.off()
button_3_led.off()
button_4_led.off()

while True:
    while Game == True:
        Game_led.on()
        if button_1.value() == 0:
            button_1_led.on()
            Game = False
        elif button_2.value() == 0:
            button_2_led.on()
            Game = False
        elif button_3.value() == 0:
            button_3_led.on()
            Game = False
        elif button_4.value() == 0:
            button_4_led.on()
            Game = False

    while Game == False:
        Game_led.off()
        if reset.value() == 0:
            button_1_led.off()
            button_2_led.off()
            button_3_led.off()
            button_4_led.off()
            Game = True

