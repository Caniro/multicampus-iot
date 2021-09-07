# domain 변수는 임의의 웹 주소를 가지고 있다.
# 이 도메인이 .kr로 끝나는 한국 도메인인지
# 확인하는 코드를 작성하라.

import random

domains = (
    "https://google.com",
    "https://naver.co.kr",
    "https://daum.net",
    "https://hrd.go.kr",
)

domain = random.choice(domains)
print(f"도메인 : {domain}")

if (domain.endswith(".kr")):
    print("한국 도메인입니다.")
else:
    print("한국 도메인이 아닙니다.")
