# 1초에 5번 온도를 측정하는 시뮬레이션

import time
import random

try:
    n = 0
    while (True):
        print(f"{n}) 온도 : {random.uniform(25, 30):.1f}도")
        time.sleep(0.2)
        n += 1
except KeyboardInterrupt:
    print("온도 측정 종료")
