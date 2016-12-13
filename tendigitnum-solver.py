# The Ten-Digit Number Puzzle
#       Find a 10-digit number where the first digit is how many zeros in the number,
#       the second digit is how many 1s in the number etc.
#       until the tenth digit which is how many 9s in the number.

# Setting up the required variables
    solutionfilelocation = 'P:/ath/of/file.txt'     # Location of the solution file that will be appended. This file needs to be created before running the script.
    solutions = list()                              # Create a list to store the results that match the rules
    number = 1000000000                             # Set the number to "zero".
    limit = 9999999999                              # Set the limit for the range to check

# The solution checking loop
    while number <= limit:
        if number % 1000000 == 0:                   # Print the number every 1,000,000 solution checks so we can see the progress.
            print (number)
        numberarray = [int(d) for d in str(number)] # Convert the number to an array so we can compare the individual elements.
                                                    # Check if the number matches the rules
        if numberarray[0] == numberarray.count(0) and numberarray[1] == numberarray.count(9) and numberarray[2] == numberarray.count(8) and numberarray[3] == numberarray.count(7) and numberarray[4] == numberarray.count(6) and numberarray[5] == numberarray.count(5) and numberarray[6] == numberarray.count(4) and numberarray[7] == numberarray.count(3) and numberarray[8] == numberarray.count(2) and numberarray[9] == numberarray.count(1):
            solutions.append(number)                # Save numbers that match the rule to a list for later use.
        number += 1                                 # Increment the number that we are checking.

# Handling the results
    file = open(solutionfilelocation, "r+")         # Open the solutions text file
    convertedsolutions = str(solutions)             # Convert our solution list into a string
    file.write(convertedsolutions)                  # Save the string to the solutions file
