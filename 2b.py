name = input("name : ")
age = int(input("age :  "))
height = float(input("height(cm) : "))
power = int(input("power : "))
collect = float(input("collect : "))


rich = 0
old = 0
strong = 0
tall = 0

if  age >= 20:
    old = 1
else:
    old = 0

if height >= 150:
    tall = 1
else:
    tall = 0

if power >= 5:
    strong = 1
else:
    strong = 0

if collect >= 5:
    rich = 1
else:
    rich = 0

print("////////////////////////////////////////////////////////////////////////////////")
print("Congratulations!, you join our team!")
print(f'Mr/Mrs.{name} || Age {age} years old || height {height} cm || power {power} || money {collect}')

if rich == 1 and old == 1 and strong == 1 and tall == 1:
    print("you are THE HEAD of our team")
elif rich == 1 and old == 0 and strong == 0 and tall == 0:
    print("you just a rich one")
elif rich == 0 and old == 0 and strong == 0 and tall == 0:
    print("i'll not let you join our team, it's to risk")
else:
    print("you are our members")

print("////////////////////////////////////////////////////////////////////////////////")
