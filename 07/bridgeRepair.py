import sys, re, os
import itertools

def partOne(inpu) :
    with open(inpu,'r') as inp :
        count=0
        for i in inp :
            valid=False
            res=re.findall("\d+",i)
            for s in itertools.product(["*","+"],repeat=len(res)-2):
#                test=eval(res[1]+"".join(["".join([x,y]) for x,y in zip(s,res[2:])]))
                test=int(res[1])
                for x,y in zip(s,res[2:]) :
#                   test=eval(str(test)+x+str(y))
                    """ eval is mega slow """
                    if x=="*" :
                        test=test*int(y)
                    elif x=="+" :
                        test=test+int(y)
                    if test>int(res[0]):
                        break
                if test==int(res[0]):
                    valid=True
                    break
            if valid :
                count+=test
    return count

print()
print("==> PART ONE <==")
print(partOne(sys.argv[1]))
print()

def partTwo(inpu) :
    with open(inpu,'r') as inp :
        count=0
        for i in inp :
            valid=False
            res=re.findall("\d+",i)
            for s in itertools.product(["*","+","||"],repeat=len(res)-2):
                test=int(res[1])
                for x,y in zip(s,res[2:]) :
                    if x=="*" :
                        test=test*int(y)
                    elif x=="+" :
                        test=test+int(y)
                    elif x=="||" :
                        test=int(str(test)+y)
                    if test>int(res[0]):
                        break
                if test==int(res[0]):
                    valid=True
                    break
            if valid :
                count+=test
    return count

print("==> PART TWO <==")
print(partTwo(sys.argv[1]))
print()

