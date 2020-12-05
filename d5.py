
def to_bin(s):
    val = 0
    for i, c in enumerate(s):
        if c in 'BR':
            val += pow(2,len(s)-1-i)

    return val

def pre_process(raw):
    row = to_bin(raw.strip()[:7])
    col = to_bin(raw.strip()[-3:])

    return(row, col)

def part1(data):
    steatID = list(map(lambda r: r[0]*8+r[1],data))
    
    print(f"Part 1: {max(steatID)}")
    return steatID

def part2(data):
    sort = sorted(data)

    for i, v in enumerate(sort):
        if abs(v - sort[i+1]) == 2:
            return print(f"Part 2: {v+1}")

data = list(map(pre_process, open("In/in5").readlines()))

part2(part1(data))