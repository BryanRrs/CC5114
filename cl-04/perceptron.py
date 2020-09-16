class Perceptron:
    def __init__(self, w, b):
        self.w = w
        self.b = b

    def out(self, x):
        r = sum([w*v for (w,v) in zip(self.w, x)]) + self.b
        return 1 if r > 0 else 0
    
    def learning(self, x, lr, diff):
        self.w = [w + (lr*x*diff) for (w,x) in zip(self.w, x)]
        self.b = self.b + (lr*diff)

