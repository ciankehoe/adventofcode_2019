# Day 1: The Tyranny of the Rocket Equation

####################
# Part 1
####################

import sys

data = sys.argv[1]  # read in our input file


def get_fuel(input):
    # read the input file as a cmd line argument
    # data = sys.argv[1]

    # initialize our "Fuel Counter-Upper" which keeps
    # track of the total fuel requirement.
    fuel_counter = 0

    with open(data) as modules:
        for mass in modules.readlines():
            mass = int(mass.strip())
            fuel_counter += (mass // 3) - 2
        return fuel_counter

    # Answer : 3320816

######################################
# Part 1 : Using map() + lambda func
######################################

def get_fuel_short(input):
    with open(data) as d:
        input = d.read().split("\n")
        fuel = sum(map(lambda x: (int(x) / 3) - 2, input))
        return fuel

######################################
# Part 2 --> Extension of Part 1
######################################

def get_more_fuel(data):
    # read the input file as a cmd line argument
    # data = sys.argv[1]

    # initialize our "Fuel Counter-Upper" which keeps
    # track of the total fuel requirement for all
    # modules, and for each modules fuel.
    total_fuel = 0

    with open(data) as modules:
        for mass in modules.readlines():
            mass = int(mass.strip())

    # loop calculating individual module fuel
    # Initialize the total amount of fuel required per module
            mod_fuel = 0
            fuel_count = (mass // 3) - 2
            while fuel_count > 0:
                mod_fuel += fuel_count
                fuel_count = (fuel_count // 3) - 2

    # increment the total fuel by the total fuel per module
            total_fuel += mod_fuel
        return total_fuel

    # Answer : 4978360

#############################################

print("Part 1) Answer : {:>29}".format(get_fuel(data)))
print("Part 1 - Shorter Solution) Answer : {:>10}".format(get_fuel_short(data)))
print("Part 2) Answer : {:>29}".format(get_more_fuel(data)))
