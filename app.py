import sys

products = [
    ("book", 12000),
    ("note", 8000),
    ("pen", 1500),
    ("bag", 25000),
    ("cup", 6000)
]
names  = [i[0] for i in products]
price = [i[1] for i in products]

def quote(price, quantity, shipping = 3000):
    subtotal = price * quantity
    if subtotal >= 30000 and is_member:
        shipping = 0
        total = subtotal + shipping
        # print("무료배송")
        print(total)
    else:
        total = subtotal + shipping
        # print("배송비 3000원")
        print(total)
    return total

def sum_values(*args):
    return sum(args)

print("파이썬 콘솔 애플리케이션")
print("수업 시간: 60")
print(sys.executable)
print("================================")


owned_items = {"book", "note", "bag"}
wish_items  = {"note", "pen"}

while True:
    print("=== 파이썬 스마트 스토어 & 학습 매니저 ===")
    print("1. 상품 목록 보기 (가격 정렬)")
    print("2. 주문 담기 및 견적 계산")
    print("3. 수량 일괄 정산 리포트 (컴프리헨션)")
    print("4. 보유 vs 관심 상품 비교 (집합 연산)")
    print("5. 주문 내역 JSON 저장 및 불러오기")
    print("6. 회원 프로필 / 추가 메모 등록 (**kwargs)")
    print("0. 종료")
    menu = input("메뉴 선택: ")

    if menu == "1":
        product = sorted(products, key=lambda item : item[1], reverse=True)
        print(product)
        print("최고가 상품: ", product[0])
        print("추천 TOP 3: ", product[:3])
        print("================================")

    elif menu == "2":
        name = input("사용자 이름: ").strip()
        is_member = input("회원 여부: ").strip()
        if is_member == "y":
            is_member = True
        elif is_member == "n":
            is_member = False
        else:
            is_member = False
        product = input("주문할 상품: ").split(",")
        amounts = input("수량: ").split(",")
        for i in amounts:
            try:
                for n in product:
                    if n in names:
                        names_idx = names.index(n)
                        prices_idx = price[names_idx]
            except ValueError:
                print("정수를 입력하세요")
            quote(prices_idx, int(i))

        print("================================")

    elif menu == "3":
        amount_list = [2, 3, 0, -1, 1]
        number = [i for i in amount_list if i > 0]

        print("================================")

    elif menu == "4":
        print(sorted(owned_items & wish_items))
        print(sorted(owned_items - wish_items))
        print(sorted(owned_items | wish_items))
        print("================================")

    elif menu == "5":
        print()

    elif menu == "6":
        point = (10, 20)
        x, y = point
        print(x, y)

    elif menu == "0":
        break