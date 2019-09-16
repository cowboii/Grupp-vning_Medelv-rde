numMax = 0
numMin = 0
count = 0
sum = 0

play = True

while(play) :
    store = input("Skriv in ett värde: ")
    try :
        float(store)
    except :
        break
    if (store == "0") :
        break
    store = float(store)

    sum += store
    count += 1

    if (count == 1) :
        numMax, numMin = store, store
    elif (store < numMin) :
        numMin = store
    elif (store > numMax) :
        numMax = store

if (count > 2) :
    totalSum = sum - numMax - numMin
    print(totalSum / (count - 2))
elif count > 0 :
    print(sum / count)
else :
    print("ERROR")