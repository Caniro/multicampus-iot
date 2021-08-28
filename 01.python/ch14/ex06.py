from pprint import pprint

def load_file(file_path):
    with open(file_path, "rt", encoding="UTF-8") as f:
        load_file = f.readlines()
        result = []
        for row in load_file:
            row = row.strip()
            if (not row):
                continue
            result.append(row.split(","))
        return result

def save_book(file, book):
    with open(file, "wt", encoding="UTF-8") as f:
        for line in book:
            line_str = ','.join(line)
            f.write(line_str + '\n')

filename = "addressbook.txt"

try:
    book = load_file(filename)
    print("\t메일로 정렬")
    book.sort(key=lambda info: info[1])
    pprint(book)
    print("\t이름으로 정렬")
    book.sort()
    pprint(book)
    save_book(filename, book)
except Exception as e:
    print(e)
