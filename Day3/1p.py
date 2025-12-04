input = []

with open("input.txt") as file:
    input = [x.strip('\n') for x in file.readlines()]
print(input)
results = []

for line in input:
    first = 0
    second = 0
    first_index = 0
    line = str(line)

    for volt_index in range(0, len(line)-1):
        print(f"comparing {int(line[volt_index])} > {first}")
        if int(line[volt_index]) > first:
            print(f"{int(line[volt_index])} > {first}")
            print("assigning first to " + line[volt_index])

            first = int(line[volt_index])
            first_index = volt_index
    print('identify second')
    for volt_index in range(first_index+1, len(line)):
        print(f"comparing {int(line[volt_index])} > {second}")

        if int(line[volt_index]) > second:
            print('assigning second to ' + line[volt_index])
            second = int(line[volt_index])
    print(f'appending {first} and {second}')
    results.append(int(f'{first}{second}'))
print(results)
print(sum(results))
