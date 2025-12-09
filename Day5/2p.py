input = []
with open('input.txt') as file:
    input = [x.strip('\n') for x in file.readlines()]

#print(input.index(''))
ranges = input[:input.index('')]
ranges = sorted([[int(y) for y in x.split('-')] for x in ranges])
items = [int(x) for x in input[input.index('') + 1:]]
output = 0

#process ranges first
final_ranges = [ranges.pop(0)]
for r in ranges:
    print(f'testing {r}')
    for rf in range(0, len(final_ranges)):
        print(final_ranges[rf])
        #track if we made any update
        updated = False
        #if our range to incorporate has lower bound in our range
        if final_ranges[rf][0] <= r[0] <= final_ranges[rf][1] + 1:
            print(f'{r[0]} within existing range')
            #and the upper bound extends further up
            if r[1] > final_ranges[rf][1]:
                #adjust range upward
                final_ranges[rf][1] = r[1]
                print('updating upper bound')
                updated = True
                break
            elif r[1] <= final_ranges[rf][1]:
                #else if its also within the range
                print('new range upper bound is within existing range')
                updated = True
                break
        #if our range to incorporate has upper bound in our range
        if final_ranges[rf][0] - 1 <= r[1] <= final_ranges[rf][1]:
            print(f'{r[1]} within existing range')
            #and the lower bound extends further down
            if r[0] < final_ranges[rf][0]:
                final_ranges[rf][0] = r[0]
                print('updating lower bound')
                updated = True
                break
            elif r[0] >= final_ranges[rf][0]:
                updated = True
                break
            
    if not updated:
        print('{r} not detected, adding net new')
        #if we never updated any ranges, we just add it to the list
        final_ranges.append(r)
    print(f'final_ranges: {final_ranges}')



print(final_ranges)
#process the final_ranges
for r in final_ranges:
    output += r[1] - r[0] + 1

print(output)


