total = 30000
is_member = False
if total < 0:
    message = "금액 오류"
elif total >= 30000 and is_member:
    message = "무료배송"
else:
    message = "배송비 3000원"
print(message)