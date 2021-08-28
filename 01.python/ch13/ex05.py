from random import choice

def connect():
    try:
        print("네트워크 접속")
        a = 2 / choice((0, 2))
        print("네트워크 통신 수행")
    except Exception as e:
        print(f"에러 : {e}")
    finally:
        print("접속 해제")
        
    print("작업 완료\n")

connect()
connect()
connect()
