name = input("name : ") 
age = int(input("age :  "))
if age >= 20:
    print("PASSED")
else:
    print("Too young")
height = float(input("height(cm) : "))
if height >= 150:
    print("PASSED")
else:
    print("Too SHORT")
power = int(input("power : "))
if power >= 5:
    print("PASSED")
else:
    print("Too Weak")
collect = float(input("collect : "))
if collect >= 5:
    print("PASSED")
else:
    print("Too Poor")

print("Congratulation, Welcome to ours team!!")
print(f'Mr/Mrs.{name} || Age {age} years old || height {height} cm || power {power} || money {collect}')