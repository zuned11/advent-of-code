input = []
with open('input.txt') as file:
    input = [x.strip('\n') for x in file.readlines()]

#print(input.index(''))
ranges = input[:input.index('')]
ranges = [[int(y) for y in x.split('-')] for x in ranges]
items = [int(x) for x in input[input.index('') + 1:]]
output = 0

print(ranges)
print(items)

for item in items:
    for range in ranges:
        if range[0] <= item <= range[1]:
            print(f"{range[0]} <= {item} <= {range[1]}")
            output += 1
            break

print(output)
