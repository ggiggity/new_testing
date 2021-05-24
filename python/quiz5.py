from random import*
count = 0
for x in range(1, 51):
    time = randrange(5, 51)
    if 5 <= time <=30:
        print(f"[0] {x}손님 (소모시간: {time})")
        count += 1
    else:
        print(f"[ ] {x}손님 (소모시간: {time})")
print(f"총 {count} 명의 손님")