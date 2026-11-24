def sum_value(*args):
    return sum(args)

def profile(**kwargs):
    return kwargs

print(sum_value(3, 5, 7))
print(profile(name = "민수", level = "basic"))
items = [("pen", 1500), ("book", 12000)]
print(sorted(items, key = lambda item : item[1], reverse = True))