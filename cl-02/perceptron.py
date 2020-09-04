class Perceptron:
    def __init__(self, w, b):
        self.w = w
        self.b = b

    def out(self, x):
        r = sum([w*v for (w,v) in zip(self.w, x)]) + self.b
        return 1 if r > 0 else 0


#Logical Perceptrons#
# AND door #
def andP():
    return Perceptron([1,1], -1.5)
# OR door #
def orP():
    return Perceptron([1,1], -0.5)
# NAND door #
def nandP():
    return Perceptron([-2,-2], 3)


##Tests##
per = Perceptron([1,1], 0)
assert per.out([0,1])
assert per.out([1,1])
assert not per.out([0,0])
assert not per.out([-1,1])
#### andP
AND = andP()
assert not AND.out([0,0])
assert not AND.out([0,1])
assert not AND.out([1,0])
assert AND.out([1,1])
#### orP
OR = orP()
assert not OR.out([0,0])
assert OR.out([0,1])
assert OR.out([1,0])
assert OR.out([1,1])
#### nandP
NAND = nandP()
assert NAND.out([0,0])
assert NAND.out([0,1])
assert NAND.out([1,0])
assert not NAND.out([1,1])
