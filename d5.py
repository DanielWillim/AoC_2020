
def to_bin(s):
    val = 0
    for i, c in enumerate(s):
        if c == 'B' or c == 'R':
            val += pow(2,len(s)-1-i)
            print(c, val, len(s)-i, pow(2,len(s)-1-i))

    return val

def pre_process(raw):
    row_raw = raw.strip()[:7]
    col_raw = raw.strip()[-3:]

    row = to_bin(row_raw)
    col = to_bin(col_raw)

    return(row, col)

def part1(data):
    steatID = list(map(lambda r: r[0]*8+r[1],data))
    print(max(steatID))
    return steatID

def part2(data):
    sort = sorted(data)
    print(sort)

    for i, v in enumerate(sort):
        if abs(v - sort[i+1]) == 2:
            print(i, v+1)
            break


data = list(map(pre_process, open("in5").readlines()))

part2(part1(data))

