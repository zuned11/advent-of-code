input = []
with open('input.txt') as file:
    input = file.read().splitlines()
pos: int = 50
output: int = 0

for line in input:
    print(f"{pos}, {line}, {output}")

    amplitude: int = int(line[1:])
    direction: int = 1 if line[0] == 'R' else -1

    while amplitude > 0:
        if direction == -1 and pos == 0:
            pos = 100
        pos += direction
        pos %= 100
        if pos == 0:
            output += 1
        amplitude -= 1
        

print(output)
