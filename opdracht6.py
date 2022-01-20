start = 50
erbij = 0
while True:
    print(str(start) +" + "+str(erbij)+" = "+str(start+erbij))
    start += erbij
    erbij += 1
    if start >= 1000:
        break 
    