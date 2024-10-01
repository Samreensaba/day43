import random

title = "MY Bingo Cards Generator"

numbers = []

def ran():
  number = random.randint(1,90)
  return number

def prettyprint():
  for list in myBingoCard:
    print(list)


for i in range(8):
  numbers.append(ran())

numbers.sort()

myBingoCard = [ [numbers[0], numbers[1], numbers[2]], [numbers[3], "BINGO", numbers[4]], [numbers[5], numbers[6], numbers[7]]]

prettyprint()