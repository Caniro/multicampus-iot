from random import randint
from time import sleep

class Sensor:
    def __init__(self, name, place):
        self.name = name    # 센서 이름
        self.place = place  # 설치 장소
        self.value = None   # 측정 값

    def measure(self):
        self.value = randint(0, 100)
        return self.value

class Light:
    def __init__(self, place):
        self.place = place
        self.state = False

    def on(self):
        if (self.state == False):
            self.state = True
            print(f"{self.place} 전등 켜짐")
    
    def off(self):
        if (self.state == True):
            self.state = False
            print(f"{self.place} 전등 꺼짐")

# temp = Sensor("온도", "거실")
# humi = Sensor("습도", "거실")
# while (True):    
#     humi.measure()
#     print(f"습도값 : {humi.value}")
#     sleep(1)

illu = Sensor("조도", "거실")
light_livingroom = Light("거실")
while (True):    
    illu.measure()
    print(f"조도값 : {illu.value}")
    if (illu.value < 40):
        light_livingroom.on()
    else:
        light_livingroom.off()
    sleep(1)

