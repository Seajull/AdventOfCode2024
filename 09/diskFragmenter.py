import sys, re, os
import itertools

def partOne(inpu) :
    with open(inpu,'r') as inp :
        disk=inp.readline()[:-1]
        file=[]
        space=[]
        x=0
        while x<len(disk)-1 :
            file.append(disk[x])
            space.append(disk[x+1])
            x+=2
        if len(disk)%2==1 :
            file.append(disk[-1])
            space.append("1")
        ind=0
        unpack=[]
        for i,j in zip(file,space) :
            k=0
            while k<int(i) :
                unpack.append(str(ind))
                k+=1
            k=0
            while k<int(j) :
                unpack.append(".")
                k+=1
            ind+=1
        unpack=unpack[:-1]
        rev=[x for x in unpack[::-1] if x != "."]
        compress=[]
        for i in unpack :
            if i!="." :
                compress.append(i)
            else :
                compress.append(rev.pop(0))
        comp=compress[:-unpack.count(".")]
        x=0
        count=0
        while x<len(comp) :
            count+=x*int(comp[x])
            x+=1
    return count

print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()

"""
Very slow solution, especially for part 2
"""
def partTwo(inpu) :
    with open(inpu,'r') as inp :
        disk=inp.readline()[:-1]
        file=[]
        space=[]
        x=0
        while x<len(disk)-1 :
            file.append(disk[x])
            space.append(disk[x+1])
            x+=2
        if len(disk)%2==1 :
            file.append(disk[-1])
            space.append("1")
        ind=0
        unpack=[]
        spaceind=[]
        for i,j in zip(file,space) :
            k=0
            while k<int(i) :
                unpack.append(str(ind))
                k+=1
            k=0
            if j!="0" :
                spaceind.append((int(j),len(unpack)))
            while k<int(j) :
                unpack.append(".")
                k+=1
            ind+=1
        spaceind=spaceind[:-1]
        unpack=unpack[:-1]
        rev=[x for x in unpack[::-1] if x != "."]
        compact={}
        for i in rev :
            if i not in compact :
                compact[i]=rev.count(i)
        for i in compact :
            for j in spaceind :
                if compact[i]<=j[0] :
                    if unpack.index(str(i))<=j[1]:
                        break
                    x=0
                    while x<compact[i]:
                        unpack[unpack.index(str(i))]="."
                        x+=1
                    x=0
                    ind=j[1]
                    while x<compact[i]:
                        unpack[ind]=i
                        ind+=1
                        x+=1
                    sind=spaceind.index(j)
                    spaceind[sind]=(spaceind[sind][0]-compact[i],spaceind[sind][1]+compact[i])
                    break
        x=0
        count=0
        while x<len(unpack) :
            if unpack[x]!=".":
                count+=x*int(unpack[x])
            x+=1
    return count

print("==> PART TWO <==")
print(partTwo(sys.argv[1]))
print()

