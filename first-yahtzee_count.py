import random

# Set the die count
diecount = 5
# Set the roll count
rollcounter = 0
# Set Yahztee value to "false"
yahtzee = 0

while (yahtzee != 1):
    # Increment the roll counter
    rollcounter += 1
    # Roll the die/dice
    dieroll = [random.randrange(1,7) for numberofdie in range(diecount)]
    # Print the roll (you can make it run WAY faster if you comment out this line)
    print (myarray)
    # If it's Yahztzee, do the following:
    if dieroll[0] == dieroll[1] == dieroll[2] == dieroll[3] == dieroll[4] == dieroll[0]:
        # Yay!
        print ("YAHTZEE!")
        print (rollcounter)
        # Set Yahtzee value to "true" which stops the while-loop
        yahtzee = 1
