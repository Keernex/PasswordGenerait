import random

while True:
  try:
    kilkist = int(input("Enter password length: "))
    break
  except ValueError:
    print("Please enter a valid integer.")

while True:
  namber = str.lower(input("Include numbers? (y/n) -> "))
  if namber=="y" or namber=="+" or namber=="yes":
    namber=2
    break
  elif namber=="n" or namber=="-" or namber=="no":
    namber=1
    break

while True:
  smolbk = str.lower(input("Include lower letters? (y/n) -> "))
  if smolbk=="y" or smolbk=="+" or smolbk=="yes":
    smolbk=2
    break
  elif smolbk=="n" or smolbk=="-" or smolbk=="no":
    smolbk=1
    break

while True:
  bigbk = str.lower(input("Include upper letters? (y/n) -> "))
  if bigbk=="y" or bigbk=="+" or bigbk=="yes":
    bigbk=2
    break
  elif bigbk=="n" or bigbk=="-" or bigbk=="no":
    bigbk=1
    break

while True:
  spezSM = str.lower(input("Include special characters? (y/n) -> "))
  if spezSM=="y" or spezSM=="+" or spezSM=="yes":
    spezSM=2
    break
  elif spezSM=="n" or spezSM=="-" or spezSM=="no":
    spezSM=1
    break