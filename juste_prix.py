import random
life = 4
for n in range(1):
  price = random.randint(1,11)
print(price)
while life > 0:
  input_user = int(input("entrer votre estimation : "))
  if input_user > price:
    print("Moin")
    life - 1
    continue
  elif input_user < price :
    print("Plus")
    life - 1
    continue
  else :
    print("Bravo vous avez deviner le nombre !")
    break
  