#/bin/python3 
input = []
with open('input.txt') as file:
    input = file.read().splitlines()
pos: int = 50
output: int = 0

for line in input:
    print(f"{pos}, {line}, {output}")

    amplitude: int = int(line[1:])
    direction: int = 1 if line[0] == 'R' else -1
    output += int(abs(amplitude) / 100)
    print(output)
    amplitude = amplitude % 100
    temp = pos + (amplitude * direction)
    print(temp)
    if abs(temp) == 100:
        temp %= 100
    elif abs(temp) > 100:
        output += 1
        print(output)
        temp %= 100

    if temp < 0:
        pos = 100 + temp
        if pos != 0:
            output += 1
    else:
         pos = temp

    if pos == 0:
        output += 1
    print(output)
print(output)

