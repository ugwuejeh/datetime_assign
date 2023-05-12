
# application that gives 10% profit every 24hours

initial_investment = 1000.0 # our initial investment amount #1000
import time

while True:
    profit = initial_investment * 0.1
    initial_investment += profit # initial_investment = initial_investment + profit
    # striftime() method was used to format date object
    #  %c local version of date and time
    print("Date and time:", time.strftime("%c")) 
    print("New investment amount:", initial_investment)
    time.sleep(86400) # Wait for 24 hours before repeating the loop
