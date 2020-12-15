from pprint import pprint

def part1(data):
    mem = {}

    for i,v in enumerate(data):
        mem[v] = [i] #Break if repeat number in start numbers
    
    last_num = data[-1]

    for i in range(len(data),30000000):

        if last_num in mem and len(mem[last_num]) > 1:
            x = mem[last_num]
            last_num = x[-1] - x[-2]
        else:
            last_num = 0
        
        if last_num in mem: 
            mem[last_num].append(i)
        else:
            mem[last_num] = [i]

    return last_num

#data = [0,3,6]
#data = [2,1,3] 
data = [1,0,15,2,10,13]

print(part1(data))