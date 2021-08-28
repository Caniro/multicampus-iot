class NameCard:
    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    def print(self):
        print(f"{self.name}, {self.email}, {self.phone}, {self.address}")

class AddressBook:
    def __init__(self, file_name):
        self.book = []
        self.load(file_name)
        self.sort()

    # 17장
    def __iter__(self):
        return iter(self.book)

    def load(self, file_name):
        self.book = []
        with open(file_name, "rt", encoding="UTF-8") as f:
            for line in f:
                if not line:
                    continue
                temp = line.strip().split(",")
                self.book.append(NameCard(*temp))

    def save(self, file_name):
        with open(file_name, "wt", encoding="UTF-8") as f:
            for nc in self.book:
                # temp = (nc.name, nc.email, nc.phone, nc.address)
                # f.write(','.join(temp))
                line = f"{nc.name},{nc.email},{nc.phone},{nc.address}\n"
                f.write(line)

    def add(self):
        name = input("이름 : ")
        email = input("이메일 : ")
        phone = input("전화번호 : ")
        address = input("주소 : ")
        self.book.append(NameCard(name, email, phone, address))
        self.sort()

    def print(self):
        for idx, name_card in enumerate(self.book, 1):
            print(f"{idx}) ", end="")
            name_card.print()

    def sort(self):
        self.book.sort(key=lambda nc: nc.name)

    def find(self):
        name = input("검색할 이름 : ")
        for nc in self.book:
            if (nc.name == name):
                nc.print()
                return
        print("목록에 없습니다.")

book = AddressBook("addressbook.txt")
# book.add()
# book.print()
# book.save("addressbook2.txt")
# book.find()

# 17장

for nc in book:
    nc.print()
