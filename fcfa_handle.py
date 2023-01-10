# FCFA currency by Bernardinho.Codes

def fcfa():
    number5 = float((input("You have choose Fcfa as Currency. Please enter how much you have: ")))
    if number5 == 0:
        print("Please enter a correct value!")
    else:
        word5 = input("Now enter please the wanted currency (USD-Yuan-Yen-Euro): ")
        if word5 == "USD":
            result_fcfa = number5 * 0.0016
            print("You have " +result_fcfa + " Fcfa")
        elif word5 == "Yuan":
            result_fcfa = number5 * 0.011
            print("You have " +result_fcfa + " Fcfa")
        elif word5 == "Yen":
            result_fcfa = number5 * 0.21
            print("You have " +result_fcfa + " Fcfa")
        elif word5 == "Euro":
            result_fcfa = number5 * 0.0015
            print(("You have " +result_fcfa + " Fcfa"))
        else:
            print("Could not recognize any currency.\nPlease enter the wanted currency USD-Yuan-Yen-Euro):")
                          