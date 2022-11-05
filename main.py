import random
print("Infinity Dice 🎲")
sides = int(input("How many sides?:"))
again = "yes"
def diceGame(rollDice):
  print("You rolled",random.randint(1,sides))
while again == "yes":
  diceGame(sides)  
  again = input("Roll again?")

  

