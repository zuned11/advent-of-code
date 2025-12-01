input = []
with open('input.txt') as file:
    for line in file:
        input.append(line)

start: int = 50

def turn_dial(starting_position:int, turn: str):
    print(starting_position, turn)
    amplitude: int = int(turn[1:]) % 100
    direction: int = 1 if turn[0] == 'R' else -1
    
    temp = (starting_position + (amplitude * direction)) % 100
    if temp < 0:
        return 100 + temp
    else:
        return temp

output: [int] = []
for line in input:
    new_position = turn_dial(start, line)
    start = new_position
    output.append(new_position)
print(output)
result = sum([1 for i in output if i == 0])
print(result)

