# Yen function by Bernadinho.codes 


def yen():
    number3 = float((input("You have choose Yen as Currency. Please enter how much you have: ")))
    if number3 == 0:
        print("Please enter a correct value!")
    else:
        word3 = input("Now enter please the wanted currency (USD-Fcfa-Yuan-Euro): ")
        if word3 == "USD":
            result_yen = number3 * 0.0076
            print("You have " +result_yen + " Yen")
        elif word3 == "Fcfa":
            result_yen = number3 * 4.66
            print("You have " +result_yen + " Yen")
        elif word3 == "Yuan":
            result_yen = number3 * 0.051
            print("You have " +result_yen + " Yen")
        elif word3 == "Euro":
            result_yen = number3 * 0.0071
            print(("You have " +result_yen + " Yen"))
        else:
            print("Could not recognize any currency.\nPlease enter the wanted currency USD-Yuan-Euro-Fcfa):")
                          