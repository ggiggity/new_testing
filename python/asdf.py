from random import*
user = range(1, 21)
user = list(user)

shuffle(user)
winner = sample(user, 4)
chicken = sample(winner, 1)
coffee = sample(winner, 3)

print("축하합니다")
print("치킨 - ", chicken)
print("커피 - ", coffee)
print("당첨됨")