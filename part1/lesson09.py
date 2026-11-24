import json

student = {"name" : "민수", "score" : 80}
student["score"] += 5
print(student.get("city", "미입력"))

text = json.dumps(student, ensure_ascii = False)
print(json.loads(text)["score"])

a = {"book", "pen", "book"}
b = {"pen", "bag"}
print(sorted(a & b))
print(sorted(a - b))
print(sorted(a | b))