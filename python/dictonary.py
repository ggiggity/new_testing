# list1 = [1, 2, 3, 4, 5]
# list2 = [6, 7, 8, 9, 10]

# list3 = zip(list1, list2)
# print(list(list3))

#2

# guest = {1:"changmo", 2:"lavin", 3:"keyboard", 4:"neemo"}
#  #1번방법
# print(guest[3])
# print(guest[2])
# # 2번방법
# print(guest.get(1))
# print(guest.get(4))
# #
# # print(guest[5])
# print(guest.get(6))

# #확인법
# print(4 in guest) #True
# print(10 in guest) #False

#string var
guests = {"A" : "nick", "B-5":"james", "C-4":"ron"}
print(guests["A"])
print(guests["B-5"])

print(guests)
guests["B-2"] = "tommy" #추가
guests["C-4"] = "lin" #변경

print(guests)

#삭제
del guests["C-4"]
print(guests)

#하나씩
print(guests.keys())
print(guests.values())

#따로따로
print(guests.items())

#전부삭제
print(guests.clear())