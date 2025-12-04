input = []

with open("input.txt") as file:
    input = [x.strip('\n') for x in file.readlines()]
print(input)
results = []

for line in input:
   line = str(line)
   voltages = [0, 0,0,0,0,0,0,0,0,0,0,0]
   indexes = [0,0,0,0,0,0,0,0,0,0,0,0]
   
   for iteration in range(0,12):
       print(len(line)-12+iteration)
       print(indexes[iteration])
       for volt_index in range(indexes[iteration], len(line)-11+iteration):
           print(f"comparing {int(line[volt_index])} > {voltages[iteration]}")
           if int(line[volt_index]) > voltages[iteration]:
               print(f'assigning to {line[volt_index]}')
               voltages[iteration] = int(line[volt_index])
               if iteration != len(voltages) - 1:
                  print(f'next index: {volt_index}')
                  indexes[iteration+1] = volt_index +1
   temp = ''
   for volt in voltages:
       temp += str(volt)

   print(f'appending {temp} ')
   results.append(int(temp))
print(results)
print(sum(results))
