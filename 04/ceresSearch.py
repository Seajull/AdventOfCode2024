import sys, re, os

def partOne(inpu) :
    count=0
    with open(inpu,'r') as inp :
        mat=[]
        for i in inp :
            mat.append([x for x in i[:-1]])
    x=0
#    for k in mat :
#        print(k)
#    print()
    while x<len(mat) :
        y=0
        while y<len(mat) :
#            print(mat[x][y])
            if mat[x][y]=="X" :
                count+=0
                vc=(getVoisin(mat,(x,y)))
#                print(vc)
                vcl=[mat[i[0]][i[1]] for i in vc]
                c=0
                while c<=len(vcl)-3 :
                    isx="".join([vcl[c],vcl[c+1],vcl[c+2]])
#                    print(isx)
                    if isx=="MAS": 
                        count+=1
#                        print("ljhlfjkdhlfdshlfjkdsfhjklsdqfh : "+str(x)+","+str(y))
                    c+=3
            y+=1
        x+=1
    return count

def getVoisin(mat,coord) :
    x=coord[0]
    y=coord[1]
    maxx=len(mat)
    maxy=len(mat[x])
    voisin=[]
#    print(coord)
    m=[]
    good=True
    n=1
    while n<4 : 
        m.append((x,y+n))
        n+=1
    for co in m :
        if co[0]<0 or co[1]<0 or co[0]>= maxx or co[1] >= maxy or len(m)<3:
            good=False
    if good :
        voisin+=m
    else :
        good=True
    n=1
    m=[]
    while n<4 : 
        m.append((x,y-n))
        n+=1
    for co in m :
        if co[0]<0 or co[1]<0 or co[0]>= maxx or co[1] >= maxy or len(m)<3:
            good=False
    if good :
        voisin+=m
    else :
        good=True
    n=1
    m=[]
    while n<4 : 
        m.append((x-n,y))
        n+=1
    for co in m :
        if co[0]<0 or co[1]<0 or co[0]>= maxx or co[1] >= maxy or len(m)<3:
            good=False
    if good :
        voisin+=m
    else :
        good=True
    n=1
    m=[]
    while n<4 : 
        m.append((x+n,y))
        n+=1
    for co in m :
        if co[0]<0 or co[1]<0 or co[0]>= maxx or co[1] >= maxy or len(m)<3:
            good=False
    if good :
        voisin+=m
    else :
        good=True
    n=1
    m=[]
    while n<4 : 
        m.append((x+n,y+n))
        n+=1
    for co in m :
        if co[0]<0 or co[1]<0 or co[0]>= maxx or co[1] >= maxy or len(m)<3:
            good=False
    if good :
        voisin+=m
    else :
        good=True
    n=1
    m=[]
    while n<4 : 
        m.append((x+n,y-n))
        n+=1
    for co in m :
        if co[0]<0 or co[1]<0 or co[0]>= maxx or co[1] >= maxy or len(m)<3:
            good=False
    if good :
        voisin+=m
    else :
        good=True
    n=1
    m=[]
    while n<4 : 
        m.append((x-n,y+n))
        n+=1
    for co in m :
        if co[0]<0 or co[1]<0 or co[0]>= maxx or co[1] >= maxy or len(m)<3:
            good=False
    if good :
        voisin+=m
    else :
        good=True
    n=1
    m=[]
    while n<4 : 
        m.append((x-n,y-n))
        n+=1
    for co in m :
        if co[0]<0 or co[1]<0 or co[0]>= maxx or co[1] >= maxy or len(m)<3:
            good=False
    if good :
        voisin+=m
    else :
        good=True
    validc=[]
    for i in voisin :
        if i[0]<0 or i[1]<0 or i[0]>= maxx or i[1] >= maxy :
            continue
        else :
#            valid.append(mat[i[0]][i[1]])
            validc.append(i)
    return(validc)


print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()

def partTwo(inpu) :
    count=0
    with open(inpu,'r') as inp :
        mat=[]
        for i in inp :
            mat.append([x for x in i[:-1]])
    x=0
#    for k in mat :
#        print(k)
#    print()
    while x<len(mat) :
        y=0
        while y<len(mat) :
#            print(mat[x][y])
            if mat[x][y]=="A" :
                count+=0
                vc=(getVoisin(mat,(x,y)))
#                print(vc)
                vcl=[mat[i[0]][i[1]] for i in vc]
                a="".join(vcl[0:3])
                b="".join(vcl[3:])
                if a=="MAS" or a[::-1]=="MAS" :
                    if b=="MAS" or b[::-1]=="MAS" :
                        count+=1
            y+=1
        x+=1
    return count

def getVoisin(mat,coord) :
    x=coord[0]
    y=coord[1]
    maxx=len(mat)
    maxy=len(mat[x])
    voisin=[]
#    print(coord)
    m=[]
    m.append((x-1,y-1))
    m.append((x,y))
    m.append((x+1,y+1))
    good=True
    for i in m :
        if i[0]<0 or i[1]<0 or i[0]>= maxx or i[1] >= maxy :
            good=False
    if good:
        voisin+=m
    else :
        good=True
    m=[]
    m.append((x-1,y+1))
    m.append((x,y))
    m.append((x+1,y-1))
    good=True
    for i in m :
        if i[0]<0 or i[1]<0 or i[0]>= maxx or i[1] >= maxy :
            good=False
    if good:
        voisin+=m
    else :
        good=True
    validc=[]
    for i in voisin :
        if i[0]<0 or i[1]<0 or i[0]>= maxx or i[1] >= maxy :
            continue
        else :
#            valid.append(mat[i[0]][i[1]])
            validc.append(i)
    return(validc)

print("==> PART TWO <==")
print(partTwo(sys.argv[1]))
print()

