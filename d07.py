from pprint import pprint
import networkx as nx

bags = {}

def to_key(w1, w2):
    return f"{w1} {w2}"

def pre_process(raw):
    ws = raw.strip().split(" ")
    k = to_key(ws[0], ws[1])
    
    bags[k] = []

    for i in range(4, len(ws),4):
        if "no" in ws[i]:
            return
        
        bags[k].append((k, to_key(ws[i+1], ws[i+2]), int(ws[i])))

def part1(bag,bags):
    g = nx.DiGraph()

    list(map(lambda w: g.add_node(w), bags.keys()))
    list(map(lambda bag: g.add_weighted_edges_from(bags[bag]), bags.keys()))
    
    return len(nx.ancestors(g, bag)), g

def part2(bag, dag):
    return sum(map(lambda dec: dag.edges[bag, dec]["weight"] * part2(dec, dag), 
                   dag.successors(bag))) + 1

list(map(pre_process, open("In/in7").readlines()))

nr, g = part1("shiny gold", bags)

print(f"Part 1: {nr}")
print(f"Part 2: {part2('shiny gold', g) - 1}")

