input: [str] = []
with open('input.txt') as file:
    input = [x.strip('\n') for x in file.read().split(',')]

invalid_ids: [int] = []

for range in input:
    start, stop = range.split('-')
    x = int(start)
    while x <= int(stop):
        print(f'testing {x}')
        if len(str(x)) % 2 == 1:
            x += 1
            continue
        first_half, second_half = str(x)[:len(str(x))//2], str(x)[len(str(x))//2:]
        print(first_half, second_half)
        if first_half == second_half:
            invalid_ids.append(x)
        x += 1

print(sum(invalid_ids))

