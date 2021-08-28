class Car:
    @staticmethod
    def hello():
        print("오늘도 안전운행 합시다.")
        print(Car.count)
    
    count = 0

    def __init__(self, name):
        self.name = name
        self.serial = Car.count
        Car.count += 1

    @classmethod
    def outcount(cls):
        print(cls.count)
    
    def intro(self):
        print(f"{self.name} ({self.serial})")

print(Car.count)
pride = Car("프라이드")
korando = Car("코란도")
Car.outcount()

print(Car.count)
Car.count = 100
Car.outcount()

pride.intro()
korando.intro()
Car.hello()

# print(f"전역 클래스 : {id(Car)}")
# print(f"클래스 변수 : {id(Car.count)}")
# print(id(pride.count))

# def dummy():
#     local_int = 2
#     local_list = list("ㅇㅅㅇㅋ")
#     print(f"전역 숫자 변수 : {id(g_a)}")
#     print(f"지역 숫자 변수 : {id(local_int)}")
#     print(f"전역 리스트 변수 : {id(g_list)}")
#     print(f"지역 리스트 변수 : {id(local_list)}")

# g_a = 1
# g_list = list("ㅇㅅㅇ")

# dummy()
