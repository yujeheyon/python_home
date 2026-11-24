name = input("이름: ").strip()
raw_quantity = input("수량: ")
quantity = int(raw_quantity)
total = quantity * 8000
print(f"{name}님, 총액: {total} 원")
print("book, pen".split(","))