import json

a = {"국어", "수학", "영어", "국어"}
b = {"과학", "수학", "사회"}

print(sorted(a & b))
print(sorted(a - b))
print(sorted(b - a))

student = {"name" : "민수", "subject" : sorted(a | b)}
print(json.dumps(student, ensure_ascii = False))