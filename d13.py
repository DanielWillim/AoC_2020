import numpy as np

def pre_process(raw):
    curr_t = int(raw[0].strip())

    raw = ",".join(raw[1:]).split(",")

    data = []
    acc = 0
    # list(map(lambda x: -1 if x in "x" else int(x), raw))

    for r in raw: 
        if r in "x":
            acc += 1
        else:                        
            data.append((acc % int(r),int(r)))
            acc += 1

    return curr_t, data

def part1(curr_t, data):
    min_t = curr_t * 5
    min_id = 0

    for (_, buss) in data: 

        depart = buss * (int(curr_t/buss)+1)

        if min_t > depart: 
            min_t = depart
            min_id = buss

    return (min_t - curr_t) * min_id

def part2(data):
    eqs = np.zeros((len(data), len(data)+1))
    b = np.zeros(len(data))
    #print(eqs)
    #print(b)

    for i, (r,buss) in enumerate(data):
        eqs[i][0]   = 1  # Num looking for
        eqs[i][i+1] = -1 * buss
        b[i] = (r + i) % buss

    print(data)

    print(eqs)
    print(b)

    # ans = np.linalg.solve(eqs,b)
    # all_done = False
    # while(not all_done):
    # #for i in range(300):
    #     all_done = True

    #     if curr_t % 100000 == 0:
    #         print(curr_t)

    #     for i, (t, buss) in enumerate(data[1:]):
    #         offset = t + i + 1
            
    #         if not (curr_t + offset) % buss == 0:
    #             curr_t += data[0][1]
    #             all_done = False
    #             break

    return curr_t

curr_t, data = pre_process(open("In/t").readlines())

print(part1(curr_t, data))
print("\n")
print(part2(data))