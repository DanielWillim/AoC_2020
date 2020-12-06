from pprint import pprint

customs_form = [{"nr": 0}]

def pre_process(line):
    if line in "\n":
        customs_form.append({"nr": 0})
        return

    customs_form[-1]["nr"] += 1

    for c in line.strip():
        if c in customs_form[-1]:
            customs_form[-1][c] += 1
        else:
            customs_form[-1][c] = 1

def part1(customs_form):
    return sum(map(len,customs_form))

def part2(customs_form):
    return sum(map(lambda group: len(list(filter(lambda l: l[0] != "nr" and l[1]==group["nr"], group.items()))), customs_form))

list(map(pre_process, open("In/in6").readlines()))



print(part1(customs_form))

print(part2(customs_form))