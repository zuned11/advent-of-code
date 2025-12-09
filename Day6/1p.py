from math import prod

input = []
with open('input.txt') as file:
    input = [x.strip('\n') for x in file.readlines()]
    input = [x.split() for x in input]

print(input)
print(len(input[0]))
print(len(input[1]))
print(len(input[2]))
print(len(input[3]))

cols = len(input[0])
rows = len(input)
print(cols, rows)
results = []

for col in range(0, cols):
    trans=[]
    #transpose each column
    for row in range(0,rows):
        trans.append(input[row][col])
    results.append(trans)

print(results)
output = []
for res in results:
    print(res)
    operation = res.pop()
    res = [int(x) for x in res]
    if operation == '+':
        output.append( sum(res))
    elif operation == '*':
        output.append( prod(res))


print(output)
print(sum(output))
