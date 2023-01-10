# Yuan function by Bernadinho.codes 


def yuan():
    number4 = float((input("You have choose Yuan as Currency. Please enter how much you have: ")))
    if number4 == 0:
        print("Please enter a correct value!")
    else:
        word4 = input("Now enter please the wanted currency (USD-Fcfa-Yen-Euro): ")
        if word4 == "USD":
            result_yuan = number4 * 0.15
            print("You have " +result_yuan + " Yuan")
        elif word4 == "Fcfa":
            result_yuan = number4 * 90.63
            print("You have " +result_yuan + " Yuan")
        elif word4 == "Yen":
            result_yuan = number4 * 19.46
            print("You have " +result_yuan + " Yuan")
        elif word4 == "Euro":
            result_yuan = number4 * 0.14
            print(("You have " +result_yuan + " Yuan"))
        else:
            print("Could not recognize any currency.\nPlease enter the wanted currency USD-Euro-Yen-Fcfa):")
                          