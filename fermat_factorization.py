#
# Fermat's Factorization Method
#
# Author: chanmile


'''
    Fermat's Factorization method relies on the following equation:
    N = a^2 - b^2 = (a+b)(a-b) 

    If (a+b) != 1 and (a-b) != 1, then N has been factored.

    Starting at a = sqrt(N), we will compute various values of b^2 using
    b^2 = a^2 - N
    
    We compute b by computing sqrt(b^2), and if b is an integer (if b is a square),
    then we have found a and b that satisfy (a+b)(a-b) and we have factored N.

From Wikipedia:
    For N with multiple prime factors, Fermat's Factorization method will return the 
    factorization with the least values of a and b. That is, a+b is the smallest factor 
    >= sqrt(N) and a-b is the largest factor <= sqrt(N)
'''


import math

def fermat_factor(composite_N):
    '''
        Please restrict usage to composite_N > 3
    '''

    lowBound_N = math.ceil(math.sqrt(composite_N))
    upBound_N  = composite_N-1

    print('Attempting to factor %s' % composite_N)
    for a in range(lowBound_N,upBound_N):

        b_squared = a**2 - composite_N
        b = math.sqrt(b_squared)

        if b.is_integer():
            print('Found factorization (%s, %s)' % (int(a+b),int(a-b)))
            return (int(a+b),int(a-b))
    return None


