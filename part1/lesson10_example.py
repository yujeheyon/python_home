raw = ["3", "x", "7", "", "12"]
numbers = []
for value in raw:
    try:
        numbers.append(int(value))
    except ValueError:
        print("건너뜀:", repr(value))
        
squares = [n * n for n in numbers if n % 2 == 1]
labels = {n: "짝수" if n % 2 == 0 else "홀수" for n in numbers}
print(numbers, squares)
print(labels)