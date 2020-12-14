from pprint import pprint

def pre_process(raw):
    if "mask" in raw:
        return ("mask", raw[7:].strip())
    
    if "mem" in raw:
        raw = list(map(lambda x: x.strip(),raw.split("=")))
        return ("mem", int(raw[0][4:-1]), int(raw[1]))

def apply_mask1(num, mask):
    num = '{0:036b}'.format(num)
    ans = ""

    for i in range(0, len(mask)):
        if mask[i] == "X":
            ans += num[i]
        
        if mask[i] in "01":
            ans += mask[i]
            
    return int(ans, 2)

def apply_mask2(addr, mask):
    addr = '{0:036b}'.format(addr)
    ans = [""]

    for i in range(0, len(mask)):
        if mask[i] == "X":
            tmp = ans.copy()
            ans = list(map(lambda x: x + "0", ans))
            tmp = list(map(lambda x: x + "1", tmp))
            ans += tmp

        if mask[i] == "1":
            ans = list(map(lambda x: x + "1", ans))
        
        if mask[i] == "0":
            ans = list(map(lambda x: x + addr[i], ans))

    return list(map(lambda x: int(x,2), ans))

def part(data, part1=True):
    mem = dict()
    mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

    for inst in data:
        if inst[0] == "mask":
            mask = inst[1]
            continue

        if inst[0] == "mem":
            if part1:
                mem[inst[1]] = apply_mask1(inst[2], mask)
            else:
                addrs = apply_mask2(inst[1],mask)

                for addr in addrs:
                    mem[addr] = int(inst[2])

    return sum(mem.values())

data = list(map(pre_process, open("In/in14").readlines()))

print(part(data))
print(part(data, part1=False))