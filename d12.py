from pprint import pprint

def pre_process(raw):
    raw = raw.strip()

    return (raw[0],int(raw[1:]))

def part1(data):
    cur_dirr = "E"
    dirs = ["N", "E", "S", "W"]
    nr_ew = 0
    nr_ns = 0

    for (inst, v) in data:
        if inst == "F":
            inst = cur_dirr
        
        if inst == "N":
            nr_ns += v
        elif inst == "S":
            nr_ns -= v
        elif inst == "E":
            nr_ew += v
        elif inst == "W":
            nr_ew -= v
        elif inst == "L":
            cur_dirr = dirs[(dirs.index(cur_dirr) - int(v/90)) % 4]
        elif inst == "R":
            cur_dirr = dirs[(dirs.index(cur_dirr) + int(v/90)) % 4]

    return abs(nr_ew) + abs(nr_ns)  

def part2(data):
    s_ew = 0
    s_ns = 0

    w_ew = 10
    w_ns = 1
    
    for (inst, v) in data:
        print(f"inst {inst} {v}, ew {s_ew}, ns {s_ew} w ew {w_ew}, w ns {w_ew}")
        if inst == "F":
            s_ew += v * w_ew
            s_ns += v * w_ns
        
        if inst == "N":
            w_ns += v
        elif inst == "S":
            w_ns -= v
        elif inst == "E":
            w_ew += v
        elif inst == "W":
            w_ew -= v
        elif inst == "L":
            x = int(v/90) % 4
            while x > 0:
                tmp = w_ew
                w_ew = -1 *  w_ns
                w_ns = tmp 
                x -= 1

        elif inst == "R":            
            x = int(v/90) % 4

            while x > 0:
                tmp = w_ew
                w_ew = w_ns
                w_ns = -1 * tmp 
                x -= 1

    return abs(s_ew) + abs(s_ns)  


data = list(map(pre_process, open("In/in12").readlines()))

print(part1(data))
print(part2(data))