input = 'input.txt'

with open(input, 'r') as file:
    freshIngredients = 0
    lines = [line.strip() for line in file]
    ranges = []
    isBreak = False
    for lineIndex, line in enumerate(lines):
        if line == '':
            isBreak = True
            continue
        if not isBreak:
            lineMin = line.split('-')[0]
            lineMax = line.split('-')[1]
            ranges.append([int(lineMin), int(lineMax)])
        elif isBreak and line != '':
            value = int(line)
            for ingredient in ranges:
                if ingredient[0] <= value <= ingredient[1]:
                    freshIngredients += 1
                    break

print(freshIngredients)
