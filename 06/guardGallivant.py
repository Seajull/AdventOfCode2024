import sys, re, os

def partOne(inpu) :
    with open(inpu,'r') as inp :
        mat=[]
        c=0
        sens=1
        out=False
        for i in inp :
            mat.append([x for x in i[:-1]])
            if "^" in i :
                posg=(c,i.index("^"))
            c+=1
        allpos=[posg]
        while not out :
            posg,sens,out,step=getInFront(posg,sens,mat) 
            for s in step :
                if s not in allpos :
                    allpos.append(s)
    return len(allpos)

def getInFront(posg,sens,mat) :
    x=posg[0]
    y=posg[1]
    maxx=len(mat)-1
    maxy=len(mat[x])
    out=False
    step=[]
    if sens==1 :
        while x!=0 :
            x-=1
            if mat[x][y]=="#" :
                posg=(x+1,y)
                break
            step.append((x,y))
    elif sens==2 :
        while y!=maxy-1 :
            y+=1
            if mat[x][y]=="#" :
                posg=(x,y-1)
                break
            step.append((x,y))
    elif sens==3 :
        while x!=maxx :
            x+=1
            if mat[x][y]=="#" :
                posg=(x-1,y)
                break
            step.append((x,y))
    elif sens==4 :
        while y!=0 :
            y-=1
            if mat[x][y]=="#" :
                posg=(x,y+1)
                break
            step.append((x,y))
    if mat[x][y]=="#" :
        sens+=1
        if sens==5 :
            sens=1
    else :
        out=True
    return posg,sens,out,step

print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()

def partTwo(inpu) :
    with open(inpu,'r') as inp :
        mat=[]
        c=0
        sens=1
        out=False
        for i in inp :
            mat.append([x for x in i[:-1]])
            if "^" in i :
                posg=(c,i.index("^"))
                iposg=(c,i.index("^"))
            c+=1
        allpos=[posg]
        while not out :
            posg,sens,out,step=getInFront(posg,sens,mat) 
            for s in step :
                if s not in allpos :
                    allpos.append(s)
        good=0
        for i in allpos : 
            out=False
            sens=1
            posg=iposg
            newmat=[]
            for j in mat :
                newmat.append(list(j))
            newmat[i[0]][i[1]]="#"
            stuck=0
            while not out :
                posg,sens,out,step=getInFront(posg,sens,newmat) 
                stuck+=1
                if stuck>1000 :
                    """ i'm a bit ashamed here, if the guard take more than 1000 direction change, it's probably because 
                    he's stuck in a loop. I found this number by increasing it incrementaly until the number of loop
                    converge to the true number, a good old and dirty brute force """
                    good+=1
                    break
    return good

def getInFront(posg,sens,mat) :
    x=posg[0]
    y=posg[1]
    maxx=len(mat)-1
    maxy=len(mat[x])
    out=False
    step=[]
    if sens==1 :
        while x!=0 :
            x-=1
            if mat[x][y]=="#" :
                posg=(x+1,y)
                break
            step.append((x,y))
    elif sens==2 :
        while y!=maxy-1 :
            y+=1
            if mat[x][y]=="#" :
                posg=(x,y-1)
                break
            step.append((x,y))
    elif sens==3 :
        while x!=maxx :
            x+=1
            if mat[x][y]=="#" :
                posg=(x-1,y)
                break
            step.append((x,y))
    elif sens==4 :
        while y!=0 :
            y-=1
            if mat[x][y]=="#" :
                posg=(x,y+1)
                break
            step.append((x,y))
    if mat[x][y]=="#" :
        sens+=1
        if sens==5 :
            sens=1
    else :
        out=True
    return posg,sens,out,step


print("==> PART TWO <==")
print(partTwo(sys.argv[1]))
print()

