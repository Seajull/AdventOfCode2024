import sys, re, os
import itertools

def partOne(inpu) :
    with open(inpu,'r') as inp :
        visited=[]
        mat=[]
        for i in inp :
            mat.append([int(x) for x in i[:-1]])
    c=0
    start=[]
    vl=[]
    for i in mat:
        s=[(c,j) for j,th in enumerate(i) if th==0]
        for z in s :
            start.append(z)
        c+=1
    for co in start :
        visited=[]
        visited=dfs(visited,mat,co)
        for coo in visited :
            vl.append(mat[coo[0]][coo[1]])
    return vl.count(9)

def dfs(visited,mat,coord):
    if coord not in visited :
        x=coord[0]
        y=coord[1]
        xmax=len(mat)
        ymax=len(mat[x])
        cur=mat[x][y]
        visited.append(coord)
        voisin=[]
        voisin.append((x,y+1))
        voisin.append((x,y-1))
        voisin.append((x+1,y))
        voisin.append((x-1,y))
        for v in voisin :
            if v[0]<0 or v[1]<0 or v[0]>=xmax or v[1]>=ymax or cur!=mat[v[0]][v[1]]-1 or v in visited: 
                continue
            dfs(visited,mat,v)
    return visited

print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()

def partTwo(inpu) :
    with open(inpu,'r') as inp :
        mat=[]
        for i in inp :
            mat.append([int(x) for x in i[:-1]])
    c=0
    start=[]
    end=[]
    for i in mat:
        s=[(c,j) for j,th in enumerate(i) if th==0]
        for z in s :
            start.append(z)
        s=[(c,j) for j,th in enumerate(i) if th==9]
        for z in s :
            end.append(z)
        c+=1
    suml=0
    for co in itertools.product(start,end) :
        st=co[0]
        en=co[1]
        suml+=len(findPath(mat,st,en))
    return suml


def findPath(mat,start,end,path=[]):
    path=path+[start]
    if start==end :
        return [path]
    paths=[]
    x=start[0]
    y=start[1]
    xmax=len(mat)
    ymax=len(mat[x])
    cur=mat[x][y]
    voisin=[]
    voisin.append((x,y+1))
    voisin.append((x,y-1))
    voisin.append((x+1,y))
    voisin.append((x-1,y))
    for v in voisin :
        if v[0]<0 or v[1]<0 or v[0]>=xmax or v[1]>=ymax or cur!=mat[v[0]][v[1]]-1 :
            continue
        if v not in path :
            npaths=findPath(mat,v,end,path)
            for np in npaths :
                if np not in paths: 
                    paths.append(np)
    return paths


print("==> PART TWO <==")
print(partTwo(sys.argv[1]))
print()

