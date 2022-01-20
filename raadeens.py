import time 
from random import seed
from random import randint
score = 0
for i in range (1,20):
    if (i != 1):
        antwoord = input("wil je nog een ronde spelen ")
        if (antwoord == "nee"):
            break
        
        print('Je score is'+str(score))

    print('ronde '+str(i))
    seed(time.time())
    randomNumber = randint(0, 1000)
    print("je mag 10 keer raden ")
    for x in range (10):
        raadgetal = input("raad een getal ")
        
        if (int(raadgetal) == randomNumber):
            print("je hebt het getal geraden ") 
            score = score +1
            break 
        elif (int(raadgetal) <= randomNumber):
            print("het getal is hoger")
            verschil = randomNumber - int(raadgetal)

            if (verschil <= 20):
                print("je bent erg warm")
            elif (verschil <= 50):
                print("je bent warm") 
            else:
                print("je bent koud")
        elif (int(raadgetal) >= randomNumber): 
            print("het getal is lager") 
            verschil = int(raadgetal) - randomNumber
            
            print(verschil)
            if (verschil <= 20):
                print("je bent erg warm")
            elif (verschil <= 50):
                print("je bent warm")
            else:
                print("je bent koud")
print(score +str(score))


