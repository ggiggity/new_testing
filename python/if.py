weather = input("how's the weather today?")
if weather == "rainy":
    print("bring an umbrella")
elif weather == "sunny"or weather == "sunshine":
    print("go naked")
elif weather == "windy":
    print("bring kite")
else:
    print("boring")

temp = int(input("what's the temperture"))
if temp <= 30:
    print("notbad")
elif 35 < temp < 45:
    print("that's hot")
elif temp <= 45 and temp < 55:
    print("i'm dying")
else:
    print("i'm in heaven")

