# Euro function from WorldCurrency

def euro():
    number1 = float((input("You have choose Euro as Currency. Please enter how much you have: ")))
    if number1 == 0:
        print("Please enter a correct value!")
    else:
        word1 = input("Now enter please the wanted currency (USD-Yuan-Yen-Fcfa): ")
        if word1 == "USD":
            result_eur = number1 * 1.07
            print("You have " +result_eur+ " Euro")
        elif word1 == "Yuan":
            result_eur = number1 * 7.27
            print("You have " +result_eur + " Euro")
        elif word1 == "Yen":
            result_eur = number1 * 141.9
            print("You have " +result_eur + " Euro")
        elif word1 == "Fcfa":
            result_eur = number1 * 660
            print(("You have " +result_eur + " Euro"))
        else:
            print("Could not recognize any currency.\nPlease enter the wanted currency USD-Yuan-Yen-Fcfa):")
                          