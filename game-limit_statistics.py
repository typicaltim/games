import random

# Set the die count
diecount = 5
# Set the number of rolls to test
rollmax = 10000000
# Set the roll count
rollcounter = 0
# Set Yahztee value to "false"
yahtzee = 0
# Set the Yahtzee counter to 0
yahtzeecounter = 0

for number in range(rollmax):
    # Increment the roll counter
    rollcounter += 1
    # Roll the die/dice
    myarray = [random.randrange(1,7) for numberofdie in range(diecount)]
    # If it's Yahztzee, do the following:
    if 6 == myarray[1] == myarray[2] == myarray[3] == myarray[4] == myarray[0]:
        yahtzeecounter += 1

# Print the results
print ("total rolls:", rollcounter)
print ("total yahztees:", yahtzeecounter)
yahtzeepercentage = yahtzeecounter / rollcounter
print ("yahtzee percentage:", yahtzeepercentage)
