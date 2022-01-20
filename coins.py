# name of student: kevin
# number of student: 
# purpose of program: Edit
# function of program: Coins
# structure of program: Coins

toPay = int(float(input('Amount to pay: '))* 100) # Het bedrag dat betaald moet worden
paid = int(float(input('Paid amount: ')) * 100) # Het bedrag dat gegeven is
change = paid - toPay # De bedragen min elkaar
bedrag = toPay - paid # het bedrag dat terug is gegeven


if change > 0: 
  coinValue = 200 #het grootste bedrag munt dat teruggeven wordt
  
  while change > 0 and coinValue > 0: #Kijkt hoeveel van elke munt er terug moet worden gegeven
    nrCoins = change // coinValue #doet min elkaar en rond het getal af

    if nrCoins > 0: #Berekent hoeveel je van alles terug moet geven 
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #Laat zien hoeveel je terug moet geven
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #Vraagt hoeveel munten je terug hebt gegeven van een bepaald coinValue!
      change -= nrCoinsReturned * coinValue #Het bedrag at terug moet gegeven worden

# comment on code below: De coins die terug kunnen gegeven worden in centen!
    if coinValue == 200:
      coinValue = 100
    elif coinValue == 100:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0


if change > 0: # Geeft aan hoeveel je nog moet gegeven al heb je niet genoeg gegeven!
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')
  print("---------------------------------------------------------  ")
  print(f"{bedrag} cent is wat u terug heeft gekregen!")
  print("---------------------------------------------------------  ")
