# from random import*
# user = range(1,21)
# user = (list(user))
# shuffle(user)

# winner = sample(user, 4)
# chicken = sample(winner, 1)
# coffee = sample(winner, 3)

# print(chicken)
from random import * 
total = 0
for x in range(1,51):
    time = randrange(5,51)
    if 5 <= time <= 15:
        print(f"[0] {x}번째 손님 (소요시간:{time})")
        total += 1
    else:
        print("[ ] {0}번째 손님 (소요시간:{1}".format(x,time))
print("총 탑승 승객 수:", total)