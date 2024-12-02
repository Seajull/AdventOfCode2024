import sys, re, os

def partOne(inpu) :
    with open(inpu,'r') as inp :
        l1=[]
        l2=[]
        count=0
        for i in inp :
            isp=i[:-1].split(" ")
            l1.append(isp[0])
            l2.append(isp[-1])
        l1.sort()
        l2.sort()
        for i,j in zip(l1,l2) :
            count+=abs(int(j)-int(i))
    return count

print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()

def partTwo(inpu) :
    with open(inpu,'r') as inp :
        l1=[]
        l2=[]
        count=0
        for i in inp :
            isp=i[:-1].split(" ")
            l1.append(isp[0])
            l2.append(isp[-1])
        for i in l1 :
            count+=int(i)*l2.count(i)
    return count

print("==> PART TWO <==")
print(partTwo(sys.argv[1]))
print()


