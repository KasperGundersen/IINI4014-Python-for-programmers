import random
import numpy as np
from random import randint
import sys
from numpy import math

def multiplicative_inverse(a, b):
    """Returns a tuple (r, i, j) such that r = gcd(a, b) = ia + jb
    """
    # r = gcd(a,b) i = multiplicitive inverse of a mod b
    #      or      j = multiplicitive inverse of b mod a
    # Neg return values for i or j are made positive mod b or a respectively
    # Iterateive Version is faster and uses much less stack space
    x = 0
    y = 1
    lx = 1
    ly = 0
    oa = a  # Remember original a/b to remove
    ob = b  # negative values from return results
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lx) = ((lx - (q * x)), x)
        (y, ly) = ((ly - (q * y)), y)
    if lx < 0:
        lx += ob  # If neg wrap modulo orignal b
    if ly < 0:
        ly += oa  # If neg wrap modulo orignal a
    # return a , lx, ly  # Return only positive values
    return lx

def decrypt(pk, ciphertext):
    # Unpack the key into its components
    key, n = pk
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr(pow(char, key) % n) for char in ciphertext]
    # Return the array of bytes as a string
    return ''.join(plain)

def PrimeGen(n=10000):
    primes = []
    chk = 2
    while len(primes) < n:
        ptest = [chk for i in range(2, chk) if chk % i == 0]
        primes += [] if ptest else [chk]
        chk += 1
    return primes


def getPrivateKey(publicKey):
    # Second nummer in the given public key
    n = publicKey[1]
    e = publicKey[0]

    # Generate primes
    primes = PrimeGen(math.sqrt(n))
    p = 0
    q = 0
    for i in primes:
        for k in primes:
            if (i*k == n):
                p = i
                q = k
    
    # Phi is the totient of n
    phi = (p-1) * (q-1)

   
    # Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)

    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))


if __name__ == '__main__':

    encryptMessage = [84620, 66174, 66174, 5926, 9175, 87925, 54744, 54744, 65916, 79243, 39613, 9932, 70186, 85020, 70186, 5926, 65916, 72060, 70186, 21706, 39613, 11245, 34694, 13934, 54744, 9932, 70186, 85020, 70186, 54744, 81444, 32170, 53121, 81327, 82327, 92023, 34694, 54896, 5926, 66174, 11245, 9175, 54896, 9175, 66174, 65916, 43579, 64029, 34496, 53121, 66174, 66174, 21706, 92023, 85020, 9175, 81327, 21706, 13934, 21706, 70186, 79243, 9175, 66174, 81327, 5926, 74450, 21706, 70186, 79243, 81327, 81444, 32170, 53121]
    publicKey = (29815, 100127)
    public, private = getPrivateKey(publicKey)

    print("Public key: ", public)
    print("Private key: ", private)
    
    print("Your message is:")
    print(decrypt(private, encryptMessage))
