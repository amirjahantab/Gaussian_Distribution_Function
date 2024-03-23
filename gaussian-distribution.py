import math
import stddraw
import sys


def phi(x):
    '''
    The standard normal cumulative distribution function.
        x is the value at which to evaluate the cumulative distribution function.
    '''
    return math.exp(-x**2 / 2.0) / math.sqrt(2.0 * math.pi)


def pdf(x, mu=0.0, sigma=1.0):
    '''
    The standard normal probability density function.
        x is the value at which to evaluate the probability density function.
        mu is the mean of the distribution.
        sigma is the standard deviation of the distribution.
    '''
    return phi(x - mu) / (sigma * math.sqrt(2.0 * math.pi))


def main():
    '''
    Draw a standard normal probability density function.
        n is the number of points to use.
    '''
    n = int(sys.argv[1])
    stddraw.setXscale(-4.0, 4.0)
    stddraw.setYscale(0.0, 0.5)
    x = [0.0] * (n + 1)
    y = [0.0] * (n + 1)
    for i in range(n + 1):
        x[i] = -4.0 + 8.0 * i / n
        y[i] = pdf(x[i])
    for i in range(n):
        stddraw.line(x[i], y[i], x[i + 1], y[i + 1])
    stddraw.show()


if __name__ == '__main__':
    main()
