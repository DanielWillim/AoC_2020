from pprint import pprint

def parse_ticket(line):
    numbers =  line.strip().split(",")
    return list(map(lambda i: int(i),numbers))

def pre_process(raw):
    raws = "".join(raw).strip().split("\n\n")
    
    # Read Rules
    rules = dict()
    for rule in raws[0].strip().split("\n"):
        rule = rule.split(":")
        name = rule[0].strip()
        conds = []

        for lh in rule[1].strip().split(" or "):
            lh = lh.split("-")
            conds.append((int(lh[0]), int(lh[1])))
        
        l0 = conds[0][0]
        h0 = conds[0][1]
        l1 = conds[1][0]
        h1 = conds[1][1]

        # rules[name] = (lambda x: ((conds[0][0] <= x <= conds[0][1]) or (conds[1][0] <= x <= conds[1][1])))
        rules[name] = (lambda x: ((l0 <= x <= h0) or (l1 <= x <= h1)))
        # rules[name] = (lambda x: (1 <= x <= 3) or (conds[1][0] <= x <= conds[1][1]))

    my_ticket = parse_ticket(raws[1].split("\n")[1])

    nerby_tickets = list(map(parse_ticket, raws[2].split("\n")[1:]))

    return rules, my_ticket, nerby_tickets

def part1(rules, nerby):
    error_rate = 0

    for ticket in nerby:
        for num in ticket:
            
            if not any(map(lambda f: f(num), rules.values())):
                error_rate += num

    print(error_rate)

def part2(rules, my, nerby):
    print(len(nerby))
    nerby = list(filter(lambda ticket:   
                        any(map(lambda num: 
                                    any(map(lambda f: f(num), rules.values())), 
                                ticket)), 
                    nerby))
    print(len(nerby))
rules, my, nerby = pre_process(open("In/in16").readlines())

part1(rules, nerby)
part2(rules, my, nerby)