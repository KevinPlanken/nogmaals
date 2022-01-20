# name of student: kevin
# number of student: 
# purpose of program: terug geven van wisselgeld 
# function of program: Coins
# structure of program: Coins

coinsreturned500 = 0
coinsreturned300 = 0
coinsreturned200 = 0
coinsreturned100 = 0
coinsreturned50 = 0
coinsreturned20 = 0
coinsreturned10 = 0
coinsreturned5 = 0
coinsreturned2 = 0
coinsreturned1 = 0
toPay = int(float(input('Amount to pay: '))* 100) # Het bedrag dat betaald moet worden
paid = int(float(input('Paid amount: ')) * 100) # Het bedrag dat gegeven is
change = paid - toPay #hij rekent uit of dat je teveel heb betaaldt

if change > 0: #hij kijkt of dat je teveel hebt betaald
  coinValue = 500 #het start getal van geld
  
  while change > 0 and coinValue > 0: #hij blijft doorgaan totdat i alles terug heeft gegeven
    nrCoins = change // coinValue #hij kijkt hoeveel je munten kan geven

    if nrCoins > 0: #hij kijkt ofdat het overige getal van munten nog bestaat
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) # Laat zien hoeveel je terug moet geven
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) # Vraagt hoeveel munten je terug hebt gegeven van een bepaald coinValue!
      change -= nrCoinsReturned * coinValue # Het bedrag dat terug moet gegeven worden
    else:
      nrCoinsReturned = 0 
      
# comment on code below: De coins die terug kunnen gegeven worden in centen!
    if coinValue == 500:
      coinValue = 300
      coinsreturned500 = nrCoinsReturned
    elif coinValue == 300:
      coinValue = 200
      coinsreturned300 = nrCoinsReturned  
    elif coinValue == 200:
      coinValue = 100
      coinsreturned200 = nrCoinsReturned  
    elif coinValue == 100:
      coinValue = 50
      coinsreturned100 = nrCoinsReturned
    elif coinValue == 50:
      coinValue = 20
      coinsreturned50 = nrCoinsReturned
    elif coinValue == 20:
      coinValue = 10
      coinsreturned20 = nrCoinsReturned
    elif coinValue == 10:
      coinValue = 5
      coinsreturned10 = nrCoinsReturned
    elif coinValue == 5:
      coinValue = 2
      coinsreturned5 = nrCoinsReturned
    elif coinValue == 2:
      coinValue = 1
      coinsreturned2 = nrCoinsReturned
    else:
      coinValue = 0
      coinsreturned1 = nrCoinsReturned

if change > 0: # kijkt of dat er nog geld over is
  print('Change not returned: ', str(change) + ' cents')

  print(f"""--------------------------------------------------------
|You've returned {coinsreturned500} of 500 cent coins.  
|You've returned {coinsreturned300} of 300 cent coins.  
|You've returned {coinsreturned200} of 200 cent coins.
|You've returned {coinsreturned100} of 100 cent coins.
|You've returned {coinsreturned50} of 50 cent coins.
|You've returned {coinsreturned20} of 20 cent coins.
|You've returned {coinsreturned10} of 10 cent coins.
|You've returned {coinsreturned5} of 5 cent coins.
|You've returned {coinsreturned2} of 2 cent coins.
|You've returned {coinsreturned1} of 1 cent coins.
---------------------------------------------------------""")

