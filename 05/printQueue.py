import sys, re, os

def partOne(inpu) :
    count=0
    with open(inpu,'r') as inp :
        rule={}
        up=[]
        for i in inp :
            if "|" in i :
                isp=i[:-1].split("|")
                if isp[0] not in rule :
                    rule[isp[0]]=[isp[1]]
                else :
                    rule[isp[0]].append(isp[1])
            elif "," in i :
                up.append(i[:-1].split(","))
    for u in up :
        n=0
        good=True
        while n<len(u)-1 :
            f=u[n]
            s=u[n+1]
            if s in rule :
                if f in rule[s] :
                    good=False
            n+=1
        if good :
            count+=int(u[int(len(u)/2)])
    return count

print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()

def partTwo(inpu) :
    count=0
    with open(inpu,'r') as inp :
        rule={}
        up=[]
        for i in inp :
            if "|" in i :
                isp=i[:-1].split("|")
                if isp[0] not in rule :
                    rule[isp[0]]=[isp[1]]
                else :
                    rule[isp[0]].append(isp[1])
            elif "," in i :
                up.append(i[:-1].split(","))
    upnot=[]
    for u in up :
        n=0
        good=True
        while n<len(u)-1 :
            f=u[n]
            s=u[n+1]
            if s in rule :
                if f in rule[s] :
                    good=False
            n+=1
        if not good :
            upnot.append(u)
    for u in upnot :
        order=[0]*len(u)
        for i in u :
            c=0
            for j in u :
                if i==j :
                    continue
                if j in rule :
                    if i in rule[j] :
                        c+=1
            order[c]=i
        count+=int(order[int(len(order)/2)])
    return count


print("==> PART TWO <==")
print(partTwo(sys.argv[1]))
print()

