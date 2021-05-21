
#1
def video(*x):
    print("i won't even try" + " " + x[0])
video("barbarian", "tango", "dingo", "dongo")


#2
def food (meat):
    print(meat + "taco")

food("beef")
food("pork")
food("chicken")
food("lamb")


#3
def chain(*dain):
    print(dain[2])

chain("lee", "roy", "choi", "doi")


#4
def coin(bit1,bit2,bit3,bit4):
    print(bit1, bit3)

coin(bit1 = "btc", bit2 = "etc", bit3 = "eth", bit4 = "ada")


#5
def doing(**what):
    print("hi" + " "+ what["what2"])

doing(what1 = "idk", what2 = "youdontknow", what3 = "chain")

#6
def tent(low = "high"):
    print(low)

tent("tie")
tent("bye")
tent("why")
tent("lie")

#7
def lame(tame):
    for rome in tame:
        print(rome)

tomb = [1, 2, 3, 4, 5]

lame(tomb)

def hi(bye):
    return "abbb"*bye

print(hi(3))
