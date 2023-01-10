# USD function by Bernadinho.codes 


def usd():
    number2 = float((input("You have choose USD as Currency. Please enter how much you have: ")))
    if number2 == 0:
        print("Please enter a correct value!")
    else:
        word2 = input("Now enter please the wanted currency (Yen-Fcfa-Yuan-Euro): ")
        if word2 == "Yen":
            result_usd = number2 * 131.89
            print("You have " +result_usd + " USD")
        elif word2 == "Fcfa":
            result_usd = number2 * 613.81
            print("You have " +result_usd + " USD")
        elif word2 == "Yuan":
            result_usd = number2 * 6.77
            print("You have " +result_usd + " USD")
        elif word2 == "Euro":
            result_usd = number2 * 0.93
            print(("You have " +result_usd + " USD"))
        else:
            print("Could not recognize any currency.\nPlease enter the wanted currency Euro-Yuan-Yen-Fcfa):")
                          