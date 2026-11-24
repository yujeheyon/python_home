datas = ["80", "abc", "50", "75", "dfg", "101"]

scores, error = [], []

for data in datas:
    try:
        score = int(data)
        if 0 <= score <= 100:
            scores.append(score)
        else:
            error.append(score)
    except ValueError:
        error.append(data)

for score in scores:
    if score >= 60:
        print(f"합격 점수: {score}")
# print(scores)
print(error)