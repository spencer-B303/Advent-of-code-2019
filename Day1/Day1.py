#%%

# take its mass,
# div by 3 
# round down 
# subtract 2

# mass: int means mass must be an iteger
def calculateFuel(mass: int):
    return mass // 3 - 2



# %%
with open('massvals.txt') as f:
    # list comp makes an int from each stripped line in txt file
    masses = [int(line.strip()) for line in f]
    part1 = sum([calculateFuel(x) for x in masses])


part1 
# %%
 
# for each module mass, calculate its fuel and add it to the total.
# treat the fuel amount you just calculated as the input mass
# continuing until a fuel requirement is zero or negative. 

z = []

def calculateFuel1(mass: int):
    y = mass // 3 - 2
    if y > 0:
        calculateFuel1(y)
        z.append(y)
    else:
        pass
    
part2 = [calculateFuel1(x) for x in masses]

part2ans = sum(z)
part2ans
# %%

# alternative solution

def fuelCalc(mass: int):
    total = 0
    
    newFuel = calculateFuel(mass)

    while newFuel > 0:
        total += newFuel
        newFuel = calculateFuel(newFuel)

    return total



part2 = sum([fuelCalc(mass) for mass in masses])
part2
# %%
