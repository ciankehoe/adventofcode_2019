# Day 1: The Tyranny of the Rocket Equation 

###########################################
# Part 1

import sys

# read the input file as a cmd line argument
data = sys.argv[1]

# initialize our "Fuel Counter-Upper" which keeps
# track of the total fuel requirement.
fuel_counter = 0

with open(data) as modules:
    for mass in modules.readlines():
        mass = int(mass.strip())
        fuel_counter += (mass // 3) - 2
    print(fuel_counter)

#############################################
# Part 2