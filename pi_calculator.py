__author__ = 'Luis Domingues'

import random
import math

#----------------------------------------------
# INPUTS
#----------------------------------------------
N = 100



#----------------------------------------------
# FUNCTIONS
#----------------------------------------------
def pi(n):
    """
    Function that determines an approximation of pi using a Monte Carlo simulation
    :param n: Number of random points
    :return: approx. of pi or None
    """
    if n > 1:
        c = 0
        for i in range(n):
            a = random.uniform(0,1)
            b = random.uniform(0,1)
            if math.sqrt((a-0.5)**2+(b-0.5)**2) < 0.5:
                c += 1
        return 4.0 * float(c) / float(n)
    else:
        return None

def print_results(pi, decimal_places=4):
    """
    Function that prints the reults
    :param pi: approximation of pi
    :return: 
    """
    if pi != None:
        s = "Approximate value for Pi: {:." + str(decimal_places) + "f}"
        print(s.format(pi))
    else:
        print("Could not determine pi")


if __name__ == "__main__":
    print_results(pi(N))