import sys, re, os

def partOne(inpu) :
    with open(inpu,'r') as inp :
        count=0
        for i in inp :
            res=re.findall("\d+",i)
            report=[int(x) for x in res]
#            print(report)
            old=""
            sens=""
            for j in report :
                safe=True
                if not old :
                    old=j
                    continue
                elif not sens :
                    if old==j:
                        safe=False
                        break
                    elif old>j:
                        if old-j>3 :
                            safe=False
                            break
                        sens="<"
                    else :
                        if j-old>3 :
                            safe=False
                            break
                        sens=">"
                    old=j
                else :
                    if old==j:
                        safe=False
                        break
                    elif old>j and sens==">" :
                        safe=False
                        break
                    elif old<j and sens=="<" :
                        safe=False
                        break
                    elif sens=="<" and old-j>3:
                        safe=False
                        break
                    elif sens==">" and j-old>3:
                        safe=False
                        break
                    old=j
#            print(safe)
            if safe :
                count+=1
    return count

print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()

def partTwo(inpu) :
    with open(inpu,'r') as inp :
        count=0
        for i in inp :
            res=re.findall("\d+",i)
            report=[int(x) for x in res]
            if not isSafe(report) :
                n=0
                while n<len(report):
                    nr=list(report)
                    nr.pop(n)
                    if isSafe(nr):
                        count+=1
                        break
                    n+=1
            else :
                count+=1
    return count

def isSafe(ln) :
    n=0
    sens=""
    while n<len(ln)-1 :
        if abs(ln[n]-ln[n+1])>3 or ln[n]==ln[n+1]:
            return False
        if not sens :
            if ln[n]>ln[n+1] :
                sens="<"
            elif ln[n]<ln[n+1] :
                sens=">"
        else :
            if ln[n]>ln[n+1] and sens==">":
                return False
            if ln[n]<ln[n+1] and sens=="<":
                return False
        n+=1
    return True

print("==> PART TWO <==")
print(partTwo(sys.argv[1]))
print()

