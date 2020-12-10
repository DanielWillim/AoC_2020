
def part1(data):
    nr_1 = 1 # From 0 to first elem
    nr_3 = 1 # From last elem to device
    
    for i, v in enumerate(data):
        if i == len(data) - 1:
            break

        if data[i+1] - v == 1:
            nr_1 += 1
        elif data[i+1] - v == 3:
            nr_3 += 1

    return nr_1*nr_3

def comb(poss, next_v):
    diffs = list(filter(lambda x: x<=3,map(lambda x: next_v - x, poss)))
    
    if len(diffs) == 3:
        return 7

    if len(poss) - len(diffs) == 2:
        return 4
    
    return 2

def part2_r(data):
    print(data)

    curr = 0
    i = 0
    poss = []
    nr = 1

    while i < len(data) : 
        v = data[i]
        diff = v - curr
        
        if diff <= 3:
            print(f"i {i}, v {v}, curr {curr}, diff {diff}")
            poss.append(v)

        elif len(poss) > 1:
            print(f"poss {poss}, comb {comb(poss, v)}")
                        
            # Do Stuff
            nr *= comb(poss, v)

            curr = poss[-1]
            poss = []
            continue
            
        elif len(poss) == 1:
            print(poss)

            curr = poss[-1]
            poss = []
            continue

        i += 1    
        
    print(f"Finished {nr}")
    return nr

data = list(map(int, open("In/t").readlines()))
data = sorted(data)

print(part1(data))
print("----")
part2_r(data)
# print(part2(data, 0, data[-1]+3))