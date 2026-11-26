import csv
import io

# 대문자 변수명을 사용하면 변경하지 않을 상수라는 의미
FIELDS = ['product', 'quantity', 'price']

def parse_sales(raw):
    # 큰 숫자를 읽기 쉽게 하기 위해 _로 구별
    if len(raw) > 100_000:
        # raise는 의도적으로 오류를 발생시키는 예약어
        # Value Error는 값이 적절하지 않을 때 사용하는 예외 종류
        raise ValueError("파일은 100KB 이하로 준비하세요.")
    try:
        # 받아온 바이트 데이터를 일반적인 문자열 형태로 변환
        # encode() : 문자열을 바이트로 변환
        # decode() : 바이트를 문자열로 변환
        text = raw.decode("utf-8-sig")
        # DictReader : CSV를 딕셔너리 형태로 읽기
        # io.StringIO() : 문자열을 파일처럼 읽도록 변환
        # strict = True : CSV 문법을 엄격하게 검사
        reader = csv.DictReader(io.StringIO(text), strict= True)

        if reader.fieldnames != FIELDS:
            raise ValueError("필수 열 순서: product, quantity, price")
        rows = []
        for number, source in enumerate(reader, 2):
            print(source)
            if len(rows) >= 1000:
                raise ValueError("데이터는 1000행 이하로 준비하세요.")
            if set(source) != set(FIELDS) or None in source.values():
                raise ValueError(f"{number}번째 레코드의 열을 확인하세요.")
            product = source["product"].strip()
            if not product or len(product) > 40:
                raise ValueError("상품명은 1~40글자입니다.")
            numeric = []
            for name in ("quantity", "price"):
                value = source[name].strip()
                if not value.isascii() or not value.isdecimal():
                    raise ValueError(f"{name}에는 양의 정수를 입력하세요.")
                value = int(value)
                if not 1 <= value <= 1_000_000:
                    raise ValueError(f"{name}은 1~1000000 범위입니다.")
                numeric.append(value)
            rows.append(dict(product = product, quantity = numeric[0], price = numeric[1]))
        return rows
    except UnicodeDecodeError as exc:
        raise ValueError("UTF-8 CSV를 사용하세요.") from exc
    except csv.Error as exc:
        raise ValueError("CSV 형식을 확인하세요.") from exc

def summarize(rows):
    by_product = {}
    for row in rows:
        name = row["product"]
        by_product[name] = by_product.get(name, 0) + row["quantity"] * row["price"]
    return {"revenue":sum(by_product.values()),
            "quantity":sum(row["quantity"] for row in rows),
            "by_product":by_product}