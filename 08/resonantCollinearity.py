import sys, re, os
import itertools

def partOne(inpu) :
    with open(inpu,'r') as inp :
        mat=[]
        for i in inp :
            mat.append([x for x in i[:-1]])
        x=0
        anloc={}
        antiloc=[]
        while x<len(mat) :
            y=0
#            print("".join(mat[x]))
            while y<len(mat[x]) :
                if mat[x][y]=="." :
                    y+=1
                    continue
                if mat[x][y] not in anloc :
                    anloc[mat[x][y]]=[(x,y)]
                else :
                    anloc[mat[x][y]].append((x,y))
                y+=1
                pass
            x+=1
        for ant in anloc :
            combi=itertools.combinations(anloc[ant],2)
            for c in combi :
                for pos in getAntinode(mat,c) :
                    if pos not in antiloc :
                        antiloc.append(pos)
    return len(antiloc) 

def getAntinode(mat,c) :
    a1=c[0]
    a2=c[1]
    la=[]
    maxx=len(mat)-1
    distance=(a1[0]-a2[0],a1[1]-a2[1])
    valid=True
    anti1=(a1[0]+distance[0],a1[1]+distance[1])
    anti2=(a2[0]-distance[0],a2[1]-distance[1]) 
    for a in anti1 :
        if a<0 or a>maxx :
            valid=False
    if valid :
        la.append(anti1)
    valid=True
    for a in anti2 :
        if a<0 or a>maxx :
            valid=False
    if valid :
        la.append(anti2)
    return la



print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()

def partTwo(inpu) :
    with open(inpu,'r') as inp :
        mat=[]
        for i in inp :
            mat.append([x for x in i[:-1]])
        x=0
        anloc={}
        antiloc=[]
        while x<len(mat) :
            y=0
#            print("".join(mat[x]))
            while y<len(mat[x]) :
                if mat[x][y]=="." :
                    y+=1
                    continue
                if mat[x][y] not in anloc :
                    anloc[mat[x][y]]=[(x,y)]
                else :
                    anloc[mat[x][y]].append((x,y))
                y+=1
                pass
            x+=1
        for ant in anloc :
            if len(anloc[ant]) > 1 :
                for antpos in anloc[ant] :
                    if antpos not in antiloc :
                        antiloc.append(antpos)
            combi=itertools.combinations(anloc[ant],2)
            for c in combi :
                for pos in getAntinodeRepeat(mat,c) :
                    if pos not in antiloc :
                        antiloc.append(pos)
    nanti=len(antiloc)
    return nanti

def getAntinodeRepeat(mat,c) :
    a1=c[0]
    a2=c[1]
    la=[]
    maxx=len(mat)-1
    distance=(a1[0]-a2[0],a1[1]-a2[1])
    cur1=a1
    cur2=a2
    valid=True
    while valid :
        anti1=(cur1[0]+distance[0],cur1[1]+distance[1])
        for a in anti1 :
            if a<0 or a>maxx :
                valid=False
        if valid :
            la.append(anti1)
            cur1=anti1
    valid=True
    while valid :
        anti2=(cur2[0]-distance[0],cur2[1]-distance[1])
        for a in anti2 :
            if a<0 or a>maxx :
                valid=False
        if valid :
            la.append(anti2)
            cur2=anti2
    return la

print("==> PART TWO <==")
print(partTwo(sys.argv[1]))
print()

