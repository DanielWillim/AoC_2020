import pprint
import re
passports = [{}]

def pre_process(raw):
    if raw == "\n":
        passports.append(dict())
        return
    
    words = raw.strip().split(" ")

    for word in words:
        kv = word.split(":")
        passports[-1][kv[0]] = kv[1]

#pprint.pprint(list(open("in4").readlines()))

def part1(fields):
    nr_ok = 0
    for p in passports:
        has_fields = True

        for k in fields:
            has_fields = (k in p) and has_fields

        if has_fields:
            nr_ok += 1

    return nr_ok

def validate_data(k, p):
    if k == "byr":
        tmp = int(p[k])
        return tmp >= 1920 and tmp <= 2002
    elif k == "iyr":
        tmp = int(p[k])
        return tmp >= 2010 and tmp <= 2020
    elif k == "eyr":        
        tmp = int(p[k])
        return tmp >= 2020 and tmp <= 2030
    elif k == "hgt":
        if "in" in p[k]:
            tmp = int(p[k][:-2])
            return tmp >= 59 and tmp <= 76
        elif "cm" in p[k]: 
            tmp = int(p[k][:-2])
            return tmp >= 150 and tmp <= 193
    elif k == "hcl" and "#" in p[k] and len(p[k]) == 7:
        regex = re.compile(r'[0-9a-f]{6}')
        return bool(regex.match(p[k][1:]))
    elif k == "ecl" and len(p[k]) == 3:
        return any(map(lambda x: x in p[k], ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]))
    elif k == "pid" and len(p[k]) == 9: 
        regex = re.compile(r'[0-9]{9}')
        return bool(regex.match(p[k]))
    #return False
        
def part2(fields):
    nr_ok = 0

    for p in passports:
        if all(map(lambda x: (x in p) and validate_data(x,p), fields)):
            nr_ok += 1
            
    return nr_ok
    
list(map(pre_process, open("in4").readlines()))

print(part1(["byr", "iyr",  "eyr",  "hgt",  "hcl",  "ecl", "pid"]))
print(part2(["byr", "iyr",  "eyr",  "hgt",  "hcl",  "ecl", "pid"]))

