def pre_process(data):
    res = []
    res = list(map(lambda x: x.strip(), data))
    return res[:-1]

data = list(map(pre_process, open("In/in3").readlines()))


def count_trees(data, right, down):
    trees = 0
    i = 0 
    j = 0

    while(i < len(data)):
        if(data[i][j] == '#'):
            trees += 1
        
        i += down
        j = (j + right) % len(data[0])

    return trees

print(count_trees(data, 1,3))

prod = 1

for i, x in enumerate([(1,1), (3,1), (5,1), (7,1), (1,2)]):
    r,d = x

    prod *= count_trees(data, r, d)
    print(r,d)

print(prod)