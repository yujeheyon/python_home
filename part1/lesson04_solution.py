count = input("점수: ")
total = int(count)

if total < 0 or total > 100:
    print("점수 오류")
elif total >= 90:
    print("A")
elif total >= 80:
    print("B")
else:
    print("C")