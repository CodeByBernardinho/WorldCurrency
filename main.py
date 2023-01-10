# Currency Converter by Bernardinho.Codes
# Current currency : 
# 1 Euro - 0.0071 Yen, 0.14 Yuan , 655.96 Fcfa
# 1 Yen - Euro, Yuan, Fcfa
# 1 Yuan - Euro, Yen, Fcfa
# 1 Fcfa - Euro, Yen, Fcfa

from euro_handle import euro
from usd_handle import usd
from yuan_handle import yuan
from yen_handle import yen
from fcfa_handle import fcfa

while True:
    welcome = input("Welcome to WorldCurrency!\nPlease enter your current: ")
    if not welcome == "Euro" or welcome == "USD" or welcome == "Yen" or welcome == "Yuan" or welcome == "FCFA":
        print("I can not recognize your input. Please enter: - Euro - USD - Yen - Yuan - FCFA")
    else:
        case = welcome
        def currency(case):
            if case == "Euro":
                return euro()
            
            elif case == "USD":
                return usd()
            
            elif case == "Yen":
                return yen()
                
            elif case == "Yuan":
                return yuan()
                
            elif case == "FCFA":
                return fcfa()
                
            else:
                return "I can not recognize your input. Please enter: - Euro - USD - Yen - Yuan - FCFA"                       
     
      

