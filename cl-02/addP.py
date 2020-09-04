from perceptron import nandP

def addP(x1,x2):
    NAND = nandP()
    n1 = NAND.out([x1,x2])
    n2 = NAND.out([x1,n1])
    n3 = NAND.out([n1,x2])
    s = NAND.out([n2,n3])
    c = NAND.out([n1,n1])
    return (s,c)


#Test
assert addP(0,0) == (0,0) 
assert addP(0,1) == (1,0)
assert addP(1,0) == (1,0)
assert addP(1,1) == (0,1)
