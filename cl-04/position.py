import perceptron as per 
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return (-2*x)-3

def training(p, n, lr):
    for _ in range(n):
        zx,zy = (np.random.uniform(-25,25),np.random.uniform(-25,25))
        result = 1 if f(zx)>= zy else 0
        output = p.out([zx,zy])
        diff = result - output
        p.learning([zx,zy],lr,diff)

def results(p, n):
    reds = [[],[]]
    blues = [[],[]]
    for _ in range(n):
        zx,zy = (np.random.uniform(-25,25),np.random.uniform(-25,25))
        if p.out([zx,zy]):
            reds[0].append(zx)
            reds[1].append(zy)
        else:
            blues[0].append(zx)
            blues[1].append(zy)   
    t = np.arange(-25.,25., 1)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    # Move left y-axis and bottim x-axis to centre, passing through (0,0)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')

    # Eliminate upper and right axes
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # Show ticks in the left and lower axes only
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    plt.plot(t, f(t), 'g', reds[0], reds[1], 'ro', blues[0], blues[1], 'bo')
    plt.show()


w = [np.random.uniform(-2,2) for _ in range(2)]
b = np.random.uniform(-2,2)

p = per.Perceptron(w,b)

training(p, 2000, 0.1)
results(p, 400)
print(p.w, p.b)