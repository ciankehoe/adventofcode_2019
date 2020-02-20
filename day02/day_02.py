import copy

#############################
# Day 2: 1202 Program Alarm #
#############################

original_input = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,9,19,23,1,6,23,27,1,10,27,31,1,5,31,35,2,6,35,39,1,5,39,43,1,5,43,47,2,47,6,51,1,51,5,55,1,13,55,59,2,9,59,63,1,5,63,67,2,67,9,71,1,5,71,75,2,10,75,79,1,6,79,83,1,13,83,87,1,10,87,91,1,91,5,95,2,95,10,99,2,9,99,103,1,103,6,107,1,107,10,111,2,111,10,115,1,115,6,119,2,119,9,123,1,123,6,127,2,127,10,131,1,131,6,135,2,6,135,139,1,139,5,143,1,9,143,147,1,13,147,151,1,2,151,155,1,10,155,0,99,2,14,0,0"
p1_input = "1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,9,19,23,1,6,23,27,1,10,27,31,1,5,31,35,2,6,35,39,1,5,39,43,1,5,43,47,2,47,6,51,1,51,5,55,1,13,55,59,2,9,59,63,1,5,63,67,2,67,9,71,1,5,71,75,2,10,75,79,1,6,79,83,1,13,83,87,1,10,87,91,1,91,5,95,2,95,10,99,2,9,99,103,1,103,6,107,1,107,10,111,2,111,10,115,1,115,6,119,2,119,9,123,1,123,6,127,2,127,10,131,1,131,6,135,2,6,135,139,1,139,5,143,1,9,143,147,1,13,147,151,1,2,151,155,1,10,155,0,99,2,14,0,0"

#######################

# creating data for part 1 and part 2
p1_data = p1_input.split(",")
p2_data = original_input.split(",")

# create / partition the larger list into a list of
# smaller lists, each of length 4.
# "chunking" the data
p1_chunks = [p1_data[x:x+4] for x in range(0, len(p1_data), 4)]
p2_chunks = [p2_data[x:x+4] for x in range(0, len(p2_data), 4)]

# changes the inner lists of strings to lists of integers // experimenting
# By no means the most efficient method!
i = 0
while i < len(p1_chunks):
    p1_chunks[i] = list(map(int, p1_chunks[i]))
    p2_chunks[i] = list(map(int, p2_chunks[i]))
    i += 1

#######################

# variable i --> refers to each individual "instruction".
# each instruction is a list of 4 elements.
# e.g [1, 2, 3, 4]
# 1 is the opcode | 2, 3, 4 are the parameters.
# the three integers after the opcode indicate where
# the inputs and outputs are, not their values.


def working_computer(prog):
    """Solution to Part 1"""

    for i in prog:
        # check for opcode 99 or any unknown opcodes --> exits program
        if i[0] > 2:
            break

        # retrieve values of our inputs
        inp_1 = prog[int(i[1] / 4)][int(i[1] % 4)]
        inp_2 = prog[int(i[2] / 4)][int(i[2] % 4)]

        if i[0] == 1:  # check for add opcode
            output = inp_1 + inp_2
        if i[0] == 2:  # check for multiply opcode
            output = inp_1 * inp_2

        # process / find the position (index) for our output
        index = int(i[3] / 4)
        inner_index = int(i[3] % 4)

        # move output into correct position
        prog[index][inner_index] = output

    return prog[0][0]


def find_noun_verb(prog, target):
    """Solution to Part 2"""

    # create a deepcopy of the original 'program' (list).
    deep_prog_copy = copy.deepcopy(prog)

    # nested for loops check for every combination of noun and verb
    for noun in range(0, 100):
        for verb in range(0, 100):

            deep_prog_copy[0][1] = noun
            deep_prog_copy[0][2] = verb

            # pass our deep copy to the 'working computer'
            # calculates value at first position using new noun/verb pair
            output = working_computer(deep_prog_copy)

            if output == target:
                return noun, verb, 100 * noun + verb
            else:
                # reinitialize our copy of the original program
                deep_prog_copy = copy.deepcopy(prog)
    return "There is no matching noun/verb pair."


#######################

print("Answers\n---------------")
print("Part 1) {}".format(working_computer(p1_chunks)))
print("Part 2) (Noun, Verb, Total) --> {}".format(find_noun_verb(p2_chunks, 19690720)))
