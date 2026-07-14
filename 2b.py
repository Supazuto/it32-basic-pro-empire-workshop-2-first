name = input("name : ") 
age = int(input("age :  "))
if age >= 20:
    print("PASSED")
    height = float(input("height(cm) : "))
    if height >= 150:
        print("PASSED")
        power = int(input("power : "))
        if power >= 5:
            print("PASSED")
            collect = float(input("collect : "))
            if collect >= 5:
                print("PASSED")
                
                print("Congratulation, Welcome to ours team!!")
                print(f'Mr/Mrs.{name} || Age {age} years old || height {height} cm || power {power} || money {collect}')
            else:
                print("Too Poor")
        else:
            print("Too Weak")
    else:
        print("Too SHORT")
else:
    print("Too young")




