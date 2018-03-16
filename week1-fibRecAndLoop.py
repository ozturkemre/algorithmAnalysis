import time
import matplotlib.pyplot as plt


def fibo_rec(n):
    if n < 2:
        return n
    else:
        return fibo_rec(n-1)+fibo_rec(n-2)


def fibo_rec_graph(n):
    for i in range(n+1):
        startTime = time.time()
        fibo_rec(i)
        stopTime = time.time()
        t = (stopTime - startTime)

        print("passed time for value ", i, " is: {} secs".format(int(round(t))))
        x.append(i)
        y.append(t)

    plt.plot(x, y)
    plt.show()


def fibo_loop(n):
    a = 0
    b = 1
    c = a + b
    if n < 2:
        return n
    while n > 0:
        a = b
        b = c
        c = a + b
        n = n - 1
    return c


def fibo_loop_graph(n):
    for i in range(n+1):
        startTime = time.time()
        fibo_loop(i)
        stopTime = time.time()
        t = (stopTime - startTime)
        print("passed time for value ", i, " is: {} secs".format(int(round(t))))
        x.append(i)
        y.append(t)

    plt.plot(x, y)
    plt.show()

x = []
y = []

n = 40
# fibo_rec_graph(n)
fibo_loop_graph(n)

