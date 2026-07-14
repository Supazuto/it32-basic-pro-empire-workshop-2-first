print("Caculate profit weapon's black market")
print("/////////////////////////////////////")

quantity_weapon = int(input("How many weapon we have? : "))
cost_price = float(input("What price per each? : "))
sell_price = float(input("How much should we sell? : "))
team_members = int(input("How many for ours team? : "))

print("/////////////////////////////////////")

all_weapon_cost = cost_price * quantity_weapon
outcome = quantity_weapon * sell_price
profit =  outcome - all_weapon_cost
for_boss = profit * 0.8
per_guys = profit * 0.2
for_guys = per_guys / team_members

print(f'All Cost {quantity_weapon} || Outcome {outcome} || Profit {profit} || How many boss will get {for_boss} || How many we guy will get (per peson) {for_guys}')