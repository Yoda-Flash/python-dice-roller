from dice import Dice

d = input("What sided dice would you like to roll? (4, 6, 8, 10, 12, 20, 100)")

result = Dice.roll(d)

print(result)