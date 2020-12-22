def pre_process(raw):
    raw = raw.strip().split(' ')
    res = []

    for r in raw: 
        tmp = []

        if '(' in r:
            i = 0
            while r[i] == '(':
                res.append(r[i])
                i += 1
            r = r[i:]

        if ')' in r:
            i = len(r) - 1

            while r[i] == ')':
                tmp.append(r[i])
                i -= 1
            r = r[:i+1]
        
        if '+' == r or '*' == r:
            res.append(r)
            continue
        
        res.append(int(r))

        if len(tmp) > 0:
            res = res + tmp

    return res

def calc1(xs):
    res = xs[0]
    i = 1
    
    while i < len(xs):
        if xs[i] in "+":
           res += xs[i+1]

        if xs[i] in "*":
            res *= xs[i+1]
        
        i += 2
    
    return res

def calc2(xs):
    # Pass 1, calc additions only
    i = 1

    while i < len(xs):  
        if xs[i] == "+":
            tmp = xs[i-1] + xs[i+1]
            del xs[i-1:i+2]
            xs.insert(i-1,tmp)
            continue
            
        i += 2

    # Pass 2, calc mults
    return calc1(xs)

def part(data, part1):
    tot_sum = 0

    for row in data:
        scopes = [[]]

        for c in row: 
            if c == '(':
                scopes.append([])
                continue

            if c == ')':
                if part1:
                    res = calc1(scopes[-1])
                else:
                    res = calc2(scopes[-1])

                del scopes[-1]
                scopes[-1].append(res)
                continue
            
            scopes[-1].append(c)
        
        if len(scopes) != 1:
            print("SOMETHING IS WRONG")

        if part1:
            tot_sum += calc1(scopes[0])
        else:
            tot_sum +=  calc2(scopes[0])

    return tot_sum


data = list(map(pre_process, open("In/in18").readlines()))


print(f"Part 1: {part(data, part1=True)}")
print(f"Part 2: {part(data, part1=False)}")