import random 
options = ( ('piedra','papel','tijera'))
computer_wins = 0
user_wins = 0
rounds = 1
while True:
  print("*"*10)
  print( 'ROUND',rounds)
  print("*"*10)
  user_option = input("piedra, papel o tijeras: ").lower()
  
  if not user_option in options:
    print()
    print("esa opcion no es valida")
    continue  
  computer = random.choice(options)
  print("la opcion que la computadora escogio ", computer)
  print("la opcion que el usuario escogio ",user_option )
  print()
  if user_option == computer:
    print("empate")
  elif user_option == 'piedra':
    if computer == 'tijeras':
      print()
      print("piedra gana a tijera, gana el usuario")
      user_wins+=1
    else: 
      print("papel gana piedra, gana el pc.")
      computer_wins += 1
  elif user_option == 'papel':
    if computer == 'piedra':
      print("papel, le gana a piedra, gana el usuario")
      user_wins+=1
    else: 
      print("tijeras, le gana a papel, gana la pc")
      computer_wins += 1
  elif user_option == 'tijeras':
    if computer == 'piedra':
      print("piedra, le gana a tijeras, gana el pc")
      computer_wins += 1
    else: 
      print("tijeras, le gana a papel, gana el usuario")
      user_wins +=1

  if computer_wins == 2:
    print('el ganador es el PC')
    break
  if user_wins == 2:
    print('el ganador es el usuario')
    break
  rounds += 1
  