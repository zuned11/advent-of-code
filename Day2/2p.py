input: [str] = []
with open('input.txt') as file:
    input = [x.strip('\n') for x in file.read().split(',')]

invalid_ids: [int] = []

for diffs in input:
    start, stop = diffs.split('-')
    x = int(start)
    while x <= int(stop):
        print(f'testing {x}')

        max_parts = len(str(x))
        max_length = len(str(x)) // 2

        for test_length in range(1, max_length + 1):
            if len(str(x)) % test_length != 0:
 #               print(f"length of x {len(str(x))} modulo {test_length} is not 0")
                continue
            print(x, test_length)
            max_parts_at_length = int(len(str(x)) / test_length)
            print(max_parts_at_length)
            parts: [int] = []
            for section in range(0, max_parts_at_length):
                parts.append(str(x)[(section * test_length):((section + 1) * test_length)])
            print(parts)
            if all(x == parts[0] for x in parts):
                print(f"found invalid {x}")
                invalid_ids.append(x)
                break

        x += 1

print(sum(invalid_ids))

