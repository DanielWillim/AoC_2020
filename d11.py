from pprint import pprint

def pre_process(raw):
    seats = []

    for i, row in enumerate(raw):
        seats.append([])
        for s in row.strip():  
            if "." in s:
                seats[i].append([-1,0]) #Floor is -1
            elif "L" in s:
                seats[i].append([0,0]) # Free is 0
            else:
                print("WRONG")

    return seats

def print_rows(data):
    for row in data:
        print(row)

def count_n(data,i,j):
    #print("-----------")
    nr = 0
    for t_i in range(i-1,i+2):
        if t_i >= len(data) or t_i < 0:
            continue
        
        for t_j in range(j-1, j+2):
            if t_j >= len(data[t_i]) or t_j < 0 or (t_j == j and t_i == i):
                continue    
            
            #print(f"Testing i {t_i} j {t_j} len i {len(data)} len j {len(data[i])}")
            if data[t_i][t_j][0] == 1:
                nr += 1

    #print_rows(data)
    #print(i,j, nr)
    return nr

def count_n_vis(data,i,j):
    nr = 0 #count_n(data,i,j)

    found_dir = [False, False, False, 
                 False,        False, 
                 False, False, False]

    c_r = 1

    # loop round range 2 and inc
    while(not all(found_dir)):
        combs = [(i-c_r, j-c_r), (i-c_r, j),(i-c_r, j+c_r), 
                 (i, j-c_r),                (i,j+c_r),    
                 (i+c_r, j-c_r), (i+c_r,j), (i+c_r, j+c_r)]

        for ind, (t_i,t_j) in enumerate(combs):
            if found_dir[ind]:
                continue

            if t_i >= len(data) or t_i < 0 or t_j >= len(data[t_i]) or t_j < 0:
                found_dir[ind] = True
                continue
            
            #print(ind, t_i, t_j, data[t_i][t_j])

            if data[t_i][t_j][0] == 1:
                nr += 1
                found_dir[ind] = True
                continue
        
            if data[t_i][t_j][0] == 0:
                found_dir[ind] = True
                continue
        
        c_r += 1
    return nr
    

def part(data, lim=4, part1=True):
    changes = 1 
    nr_occupied = 0
    iters = -1

    while changes > 0:
        print("------------------------------")
        iters += 1
        #print_rows(data)
        print(f"i {iters}, changes {changes}")
        
        changes = 0

        for x, row in enumerate(data):
            for y, s in enumerate(row):
                if s[0] == -1:
                    continue

                if s[1] == 0 and s[0] == 0: # No neighbors
                    #print(f"Seated {x,y} s {s}")
                    s[0] = 1 # Occupied
                    changes += 1
                    nr_occupied += 1
                elif s[1] >= lim and s[0] == 1: #  leave seat
                    #print(f"Left {x,y} s {s}")
                    s[0] = 0
                    changes += 1
                    nr_occupied -= 1


        for i, row in enumerate(data):
            for j, s in enumerate(row):
                if part1:
                    n = count_n(data,i,j)
                else: 
                    n = count_n_vis(data,i,j)
                    #print(f"i,j {i,j} n {n}")
                
                s[1] = n

    #print_rows(data)
    return nr_occupied

data = pre_process(open("In/in11").readlines())

#pprint(part(data))

print(part(data.copy(),lim=5, part1=False))

#print_rows(data)
#print(count_n_vis(data,4,4))