first, *lines = open('input.txt')

prev = [x == 'S' for x in first]
print(prev) 
for line in lines:
    print(line)
    for i in range(len(line)):
        if line[i] == '^':
            prev[i-1] += prev[i]
            prev[i+1] += prev[i]
            prev[i] = 0

print(sum(prev))
