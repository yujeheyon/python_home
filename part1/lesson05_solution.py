total = 0

for num in range(1, 11):
    if num % 2 != 0:
        continue
    total += num
print(f"짝수 총합: {total}")

print("=====================")
total = 0
for num in range(1, 11):
    if num % 2 == 0:
        continue
    total += num
print(f"홀수 총합: {total}")

print("=====================")
number = 0
while number <= 10:
    number += 1
    if number % 2 == 0:
        print(number)

print("=====================")
number = 0
while number < 10:
    number += 1
    if number % 2 != 0:
        print(number)