class NameCard:
    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    def print(self):
        print(f"{self.name}, {self.email}, {self.phone}, {self.address}")

# book = [
#     NameCard("둘리", "dooli@gmail.com", "010-1111-3333", "경기도 안양시"),
#     NameCard("고길동","go@gmail.com","010-1111-2222","서울시 서초구"),
#     NameCard("도우너","douner@naver.com","010-1111-4444","경기도 수원시"),
#     NameCard("마이콜","mickol@daum.net","010-1111-5555","인천광역시"),
#     NameCard("홍길동","hong@gmail.com","010-1111-1111","서울시 강남구")
# ]

# addressbook.txt를 읽어서 NameCard의 리스트를 리턴하는 함수
def load(file_name):
    result = []
    with open(file_name, "rt", encoding="UTF-8") as f:
        for line in f:
            if not line:
                continue
            temp = line.strip().split(",")
            result.append(NameCard(*temp))
    return result

def print_book(book):
    for idx, name_card in enumerate(book, 1):
        print(f"{idx}) ", end="")
        name_card.print()


book = load("addressbook.txt")
book.sort(key=lambda nc: nc.address)
print_book(book)
