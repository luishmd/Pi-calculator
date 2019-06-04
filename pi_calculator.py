__author__ = 'Luis'

import random
import math


def pi(n):
    if n > 1:
        c = 0
        for i in range(n):
            a = random.uniform(0,1)
            b = random.uniform(0,1)
            if math.sqrt((a-0.5)**2+(b-0.5)**2) < 0.5:
                c +=1
        return 4 * float(c) / float(n)
    else:
        return 0


if __name__ == "__main__":
    for i in range(20):
        print(pi(i))

    print(pi(1000))