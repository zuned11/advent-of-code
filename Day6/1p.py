from math import prod

input = []
with open('input.txt') as file:
    input = [x.strip('\n') for x in file.readlines()]

print(input)
cols = len(input[0])
rows = len(input)
results = []
new_input = []

for col in range(0, cols):
    trans=[]
    #transpose each column
    for row in range(0,rows):
        trans.append(input[row][col])
    new_input.append(trans)
print(f'new_input = {new_input}')

def check_all_spaces(x: list):
    for item in x:
        if item != '' and item != ' ':
            return False
    return True
print(check_all_spaces([' ', ' ', '', '',]))

def sum_weirdly(values):
    print(f'values = {values}')
    numbers = []
    operation = values[0].pop()
    cols = len(values[0])
    rows = len(values)
    temp_str = ''
    for num in values:
        for digit in num:
            temp_str += digit
        print(f'temp_str is a {type(temp_str)} with value {temp_str}')
        numbers.append(temp_str.strip())
        temp_str = ''
    numbers = [int(x) for x in numbers]
    print(f'numbers = {numbers}')
    if operation == '+':
        return sum(numbers)
    elif operation == '*':
        return prod(numbers)


output = []
temp = []
for i in range(0, len(new_input)):
    print(new_input[i])
    if not check_all_spaces(new_input[i]):
        temp.append(new_input[i])
    else:
        print(temp)
        output.append(sum_weirdly(temp))
        temp = []
        print('wiped_temp')
output.append(sum_weirdly(temp))

print(output)
print(sum(output))
