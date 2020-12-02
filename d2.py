def pre_process(s):
    rule, data = s.split(":")
    lim, char = rule.split(" ")
    lower, upper = lim.split("-")
    lower = int(lower)
    upper= int(upper)
    return ((lower,upper, char), data.strip())

data = list(map(pre_process, open("in2").readlines()))

def part1(data):
    ok_pass = 0

    for rule, p in data: 
        lo, up, c = rule
        fil = list(filter(lambda x: x == c, p))
        if len(fil) >= lo and len(fil) <= up: 
            ok_pass += 1

    return(ok_pass)

def part2(data):
    ok_pass = 0

    for rule, p in data:         
        x = 0
        i, j, c = rule
        if p[i-1] == c:
            x += 1
        if p[j-1] == c:
            x += 1
        
        if x == 1: 
            ok_pass += 1
    
    return(ok_pass)

print(f"Part 1 {part1(data)}")
print(f"Part 2 {part2(data)}")
