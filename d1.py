numbers = list(map(lambda x: int(x.strip()), open("In/in1").readlines()))

numbers = sorted(numbers)

i = 0
j = len(numbers) - 1
target = 2020

while(i < j):
    sumN = numbers[i] + numbers[j]
    if sumN == target:
        print(numbers[i], numbers[j], numbers[i] * numbers[j])
        break
    elif sumN < target:
        i += 1
    elif sumN > target:
        j -= 1

for a in numbers:
    for b in numbers:
        for c in numbers:
            if a + b + c == target:
                print(a,b,c, a*b*c)
            

print("No sum to target")