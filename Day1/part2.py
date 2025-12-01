input = []
with open('input.txt') as file:
    for line in file:
        input.append(line)

pos: int = 50
output: int = 0

for line in input:
    print(pos, line)
    amplitude: int = int(line[1:])
    direction: int = 1 if line[0] == 'R' else -1
    output += int(abs(amplitude) / 100)   
    temp = (pos + ((amplitude%100) * direction)) % 100
    if temp < 0:
        pos = 100 + temp
    else:
         pos = temp

    if pos == 0:
        output += 1
print(output)

