import copy

spam = ["hello", "goodbye", "tonight"]
cheese = copy.copy(spam)

cheese[1] = "hello again"

print(cheese)

deep_spam = ["it's a list", ("typl", 34), "forty"]
deep_cheese = copy.deepcopy(deep_spam)

print(deep_cheese)

deep_cheese[1] = "no more tuple"

print(deep_cheese)
