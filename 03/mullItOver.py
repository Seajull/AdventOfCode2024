import sys, re, os

def partOne(inpu) :
    with open(inpu,'r') as inp :
        mul=0
        for i in inp :
            res=re.findall("mul\((\d{1,3}),(\d{1,3})\)",i)
            for k in res :
                mul+=int(k[0])*int(k[1])
    return mul

print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()

def partTwo(inpu) :
    with open(inpu,'r') as inp :
        mul=0
        do=True
        for i in inp :
            res=re.findall("mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)",i)
            for k in res :
                if "mul" in k and do :
                    n=re.findall("\d+",k)
                    mul+=int(n[0])*int(n[1])
                elif k=="don't()" :
                    do=False
                elif k=="do()" :
                    do=True
    return mul

print("==> PART TWO <==")
print(partTwo(sys.argv[1]))
print()

