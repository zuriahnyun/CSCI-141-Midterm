#Author:Zuriahn Yun
#Date: 2/10/2023
#Description:Midterm exam, CSCI 141,Spring 2023
#yunz@wwu.edu W01576882
#          Crop     Weeks    Seed Price    Sale Price
#        garlic         5         $0.08         $1.20
#        tulips         8         $0.18         $2.30

#  Weekly grocery budget: $10.0

# Your tasks are briefly listed here; see the instructions for full details.

# 1. Read the four inputs from command line arguments
# 2. Print the season length and starting account balance.
# In each week:
#   3. Harvest and sell if a crop is due for harvest
#   4. Buy seeds and (re)plant if the crop has not been (re)planted
#   5. Print the account balance
#   6. Subtract the weekly grocery budget at the beginning of each week
#   7. End the program if the user runs out of money, and print a final message
#   8 (extra credit). Support an AUTO quantity for tulips
import sys
weeks = int(sys.argv[1])
starting_balance = float(sys.argv[2])
garlic = int(sys.argv[3])
tulip = int(sys.argv[4])
garlic_money = 0.08
tulip_money= 0.18
garlic_sale=1.20
tulip_sale=2.30

print("Season length:", weeks,"weeks")
print("Starting balance:", starting_balance)
print("Planted garlic spent $ 0.8")
print("Planted tulips spent $ 1.7999999999999998")


starting_balance=starting_balance-(garlic*garlic_money)-(tulip*tulip_money)
week = 0

grocery = 10

while week != weeks+1:
    starting_balance= starting_balance-grocery
    print("Week",week,"balance", starting_balance)
    week+=1     
    if week % 5 ==0:
        starting_balance=starting_balance-(garlic* garlic_money)+(garlic*garlic_sale)
        print("Harvested garlic made $",garlic*garlic_sale)
        print("Planted garlic spent $",garlic*garlic_money)
    if week % 8 ==0:
        starting_balance=starting_balance-(tulip*tulip_money)+(tulip*tulip_sale)
        print("Harvested tulip made $",tulip*tulip_sale)
        print("Planted tulip spent $",tulip*tulip_money)
if starting_balance<0:
        print("Player ran out of money!")
if week == weeks+1 and starting_balance>0:
    print("Player ended the season with $",starting_balance)

    
    
    