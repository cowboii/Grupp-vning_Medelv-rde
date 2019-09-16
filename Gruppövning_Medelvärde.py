def medelvärde():

    num_max = 0
    num_min = 0
    sum = 0
    count = 0

    while True:
        store = input("Skriv in ett värde: ")

        try:
            store = float(store)
        except:
            print('Invalid input')
            break

        if store == 0:
            break
        else:
            sum += store
            count += 1

        if count == 1:
            num_max, num_min = store, store
            continue
        else:
            if store < num_min:
                num_min = store
            if store > num_max:
                num_max = store

    if count > 2:
        count -= 2
        sum -= num_max
        sum -= num_min
        return sum / count

    elif num_max or num_min and count > 0:
        return sum / count

    else:
        return 0


if __name__ == "__main__":
    print(medelvärde())
