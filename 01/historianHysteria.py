import sys, re, os

def partOne(inpu) :
    with open(inpu,'r') as inp :
        count=0
        for i in inp :
            res=re.findall("\d",i)
            count+=int(res[0]+res[-1])
    return count

print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()

def partTwo(inpu) :
    alpha=["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    count=0
    with open(inpu,'r') as inp :
        for i in inp :
            res=re.findall("(?=(one|two|three|four|five|six|seven|eight|nine|\d))",i)
            if res[0] in alpha :
                first=str(alpha.index(res[0])+1)
            else :
                first=res[0]
            if res[-1] in alpha :
                sec=str(alpha.index(res[-1])+1)
            else :
                sec=res[-1]
            count+=int(first+sec)
    return count

print("==> PART TWO <==")
print(partTwo(sys.argv[1]))


