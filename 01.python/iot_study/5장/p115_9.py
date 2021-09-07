while (True):
    try:
        num = int(input("정수 입력 : "))
        break
    except KeyboardInterrupt:
        exit(1)
    except:
        print("정수만 입력해주세요.")

if (num % 5 == 0):
    print("5의 배수 맞음")
else:
    print("5의 배수 아님")
