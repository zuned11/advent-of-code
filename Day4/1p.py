temp_input = []
input = []
with open('input.txt') as file:
    temp_input = [x.strip('\n') for x in file.readlines()]
    input = [[char for char in line] for line in temp_input]
for row in input:
    print(row)
def is_roll(x, y):
    return input[x][y] == '@' or input[x][y] == 'x'
results = 0
x, y = 0, 0
for x in range(0,len(input[0])):
    for y in range(0, len(input)):
        print('checking position ' + str(x) + ' '+str(y))
        if input[x][y] != '@':
            continue
        nearby_rolls = 0
        for x_mod in [-1, 0, 1]:
            for y_mod in  [-1, 0, 1]:
                if 0 <= x + x_mod < len(input[0]) and 0 <= y+y_mod < len(input) and not (x_mod == 0 and y_mod == 0):
                    print(f'checking {x+x_mod}, {y+y_mod}')
                    if is_roll(x+x_mod, y+y_mod):
                        print('roll detected')
                        nearby_rolls += 1
        print('rolls nearby' + str(nearby_rolls))
        if nearby_rolls < 4:
            input[x][y] = 'x'
            results += 1
print(results)
for row in input:
    print(row)
