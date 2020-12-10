def subset_sum2(nums, target):
    numbers = sorted(nums)

    i = 0
    j = len(numbers) - 1
    target = target

    while(i < j):
        sumN = numbers[i] + numbers[j]
        if sumN == target:
            return True
        elif sumN < target:
            i += 1
        elif sumN > target:
            j -= 1

    return False

def part1(data, window=25):
    for i in range(window, len(data)):
        if not subset_sum2(data[i-window:i], data[i]):
            return data[i]

def part2(data, target):
    s_i = 0
    e_i = 1
    while sum(data[s_i:e_i+1]) != target:
        if e_i == len(data):
            s_i += 1
            e_i = s_i + 1
        else:
            e_i += 1
        
    return min(data[s_i:e_i+1]) + max(data[s_i:e_i+1])

data = list(map(int, open("In/in9").readlines()))
target = part1(data)

print(f"Part 1: {target}")
print(f"Part 2: {part2(data, target)}")