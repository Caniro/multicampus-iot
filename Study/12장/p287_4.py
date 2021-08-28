# 1994년 5월 5일에 태어난 사람이 
# 현재 며칠째 살고 있는지 계산하는 프로그램을 작성하라.

import time
from math import ceil

birth = {
    "year": 1994,
    "month": 5,
    "day": 5
}

tm_birth = (
    birth.get("year"),
    birth.get("month"),
    birth.get("day"),
    0, 0, 0, 0, 0, 0
)

epoch_time_birth = time.mktime(tm_birth)
ellapsed_sec = time.time() - epoch_time_birth
ellapsed_day = ceil(ellapsed_sec / (24 * 60 * 60))
print(f"경과일 : {ellapsed_day}")
