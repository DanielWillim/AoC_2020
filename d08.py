from pprint import pprint

def pre_process(raw):
    return (raw[:4].strip(), int(raw[4:]))

def run_code(code):
    ran_inst = set()
    acc = 0
    i = 0

    while i != len(code):
        if i > len(code):
            return False, acc

        (inst, v) = code[i]

        if i in ran_inst:
            return False, acc

        ran_inst.add(i)

        if inst == "acc":
            acc += v        
        elif inst == "jmp":
            i += v
            continue
        
        i += 1

    return True, acc

def part1(code):
    _, acc = run_code(code)

    return acc




def part2(code, start_i=0, start_acc=0):
    for i, op in enumerate(code):
        inst, v = op
        test_code = code.copy()
        
        if inst == "acc":
            continue
        elif inst == "jmp":
            test_code[i] = ("nop", v)
        elif inst == "nop":
            test_code[i] = ("jmp", v)
        
        res, acc = run_code(test_code)
        
        if res:
            return acc

code = list(map(pre_process, open("In/in8").readlines()))

print(f"Part 1: {part1(code)}")
print(f"Part 2: {part2(code)}")