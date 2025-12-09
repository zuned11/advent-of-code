input = []
with open('input.txt') as file:
    input = [x.strip('\n') for x in file]
output = []
def process_beam(next_line, rest, splits=0):
    print(next_line)
    print(rest)
    print(splits)
    if len(rest) == 0:
        return splits
    else:
        times_split = 0
        beams = []
        for i in range(0, len(next_line)):
            if next_line[i] in ['S', '|']:
                beams.append(True)
            else:
                beams.append(False)
        print(beams)
        next = list(rest[0])
        print(next)
        for i in range(0, len(next)):
            if beams[i]:
                if next[i] == '^':
                       times_split += 1
                       next[i-1] = '|'
                       next[i+1] = '|'
                else:
                       next[i] = '|'
        output.append(next_line)
        return process_beam(next, rest[1:], splits + times_split)

                       
print(output)
result = process_beam(input[0], input[1:], 0)
print(result)
