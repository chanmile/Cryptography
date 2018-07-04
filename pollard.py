#
# Pollard's p-1 Algorithm
#
# Author: chanmile

'''
    Let <composite_N> be a composite integer with prime factor <p>.

    By fermat's little theorem, all integers <a> coprime to <p> 
        a^(p-1) === 1 mod p           # === means congruent to

    If z === 1 mod p, z-1 === 0 mod p, then z-1 shares the same factor
    <p> with <composite_N>, and computing gcd(z-1,composite_N) reveals p.

    Suppose that a number <B> exists and (p-1) divides <B>!
    It follows that <B>! = (p-1)*j
    Then z = a^(B!) === a^((p-1)*j) === 1^j mod p === 1 modp, and p is revealed.

    How do we find z?
    Successively compute z_k = z_old^k mod n, and check if 1 < d < n where d = gcd(z-1,n)
    Since z = a^(b!) = a^(b1*b2*b3...bX), z can be computed successively like so:

    z = z_old^k where 1 < k < b and z_old = 2


    Analysis:

    Pollard hinges on the fact that the number preceding the prime factor is "B powersmooth",
    A number is "B powersmooth" if none of its prime factors are greater than B.

    From Wikipedia:
        The essential objservation is that, by working in the multiplicative group modulo a 
        composite number N, we are also working in the multiplicative groups modulo all of N's factors.

    Pollard's performance will rapidly degrade if the composite_N's prime factors are large.
    If choosing composite_N above the 10^20 mark, one should consider using the Quadratic Sieve/
    General Number Field Sieve instead.

'''

from fractions import gcd

def pollard(composite_N,bound_B,expansion_X):
    '''
        Takes N=PQ where p and q are porime factors and finds the prime factorization of N.
        Arguments:
            n - composite number we wish to learn the factorization of
            B - smoothness bound B
            X - upon exhausting the smoothness bound, B = X*B
    '''

    expanded = False
    z_old = 2
    k = 1

    while( k < bound_B):
    
        z = z_old ** (k) % composite_N
        d = gcd(z-1,composite_N)    

        if 1 < d and d < composite_N:
            print('Prime factorization is (%s, %s) ' % (int(d),int(composite_N/d)))
            return (int(d),int(composite_N/d))

        if k == bound_B -1 and not expanded:
            print('Smoothness bound exhausted, expanding...')
            expanded=True
            bound_B = bound_B * expansion_X

        elif k == bound_B -1 and expanded:
            print('Smoothness bound exhausted, exiting...')

        z_old = z
        k += 1


#pollard(6715963697 , 5000, 2)
