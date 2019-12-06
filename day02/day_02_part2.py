input = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,9,19,23,1,6,23,27,1,10,27,31,1,5,31,35,2,6,35,39,1,5,39,43,1,5,43,47,2,47,6,51,1,51,5,55,1,13,55,59,2,9,59,63,1,5,63,67,2,67,9,71,1,5,71,75,2,10,75,79,1,6,79,83,1,13,83,87,1,10,87,91,1,91,5,95,2,95,10,99,2,9,99,103,1,103,6,107,1,107,10,111,2,111,10,115,1,115,6,119,2,119,9,123,1,123,6,127,2,127,10,131,1,131,6,135,2,6,135,139,1,139,5,143,1,9,143,147,1,13,147,151,1,2,151,155,1,10,155,0,99,2,14,0,0"
data = input.split(",", 4)
mydata = input.split(",")
numsplits = len(input.split(',')) // 4
######################################

def process_array(altered_list):
    for i in altered_list:
        if i[0] == 99:
            break
        inp1 = altered_list[i[1] / 4][i[1] % 4]
        inp2 = altered_list[i[2] / 4][i[2] % 4]
        if i[0] == 1: # add opcode
            new_val = inp1 + inp2
        if i[0] == 2: # multiply opcode
            new_val = inp1 * inp2
        index = i[3] / 4
        inner_index = i[3] % 4
        altered_list[index][inner_index] = new_val

    return altered_list[0][0]

chunks = [mydata[x:x+4] for x in range(0, len(mydata), 4)]

# changes a list of lists of strings to lists of integers
i = 0
while i < len(chunks):
    chunks[i] = list(map(int, chunks[i]))
    i += 1

shall_chunk = chunks

for noun in range(0, 100):
    for verb in range(0, 100):
        chunks[0][1] = noun
        chunks[0][2] = verb
        if process_array(chunks) == 19690720:
            print("YUP")
        else:
            chunks = shall_chunk
        """answer = process_array(chunks)
        print(answer)
        chunks = shall_chunk"""