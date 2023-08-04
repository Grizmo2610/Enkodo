from random import randint
import GetPrime

def gcd(a: int, b: int):
    """
    This function compute greatest common divisor between 'a' and 'b' Using Eculid Algorithm

    Parameters: 
            a(int): first number
            b(int): second number

    Return: (int) - Greatest common divisor
    """
    while b:
        a, b = b, a % b
    return a

def generateKey(p: int, q: int) -> tuple[tuple[int, int], tuple[int, int]]:
    """
    This function generate pair of key ((e, n), (n, d)) using RSA Algorithm.

    Parameters:
            p (int): A prime number
            q (int): A prime number

    Return: tuple(tuple(int, int), tuple(int, int)) - pair of key (public key, private key)
    """
    p = GetPrime.nextPrime(p)
    q = GetPrime.nextPrime(q)

    euler = (p - 1) * (q - 1)
    carmichael = euler // gcd(p - 1, q - 1)
    n = p * q

    e = 65537
    while gcd(e, carmichael) != 1:
        e = randint(2, carmichael - 1)
        
    print(e)

    d = pow(e, -1, euler)
    return (e, n), (n, d)


def randomKey(bits: int = 1024):
    """
    This method generate random key with pair p, q have length of bits with minium is 8

    Parameter:
            bits (int): an integer number

    Return: tuple(tuple(int, int), tuple(int, int)) - pair of key (public key, private key)
    """
    bits = max(8, bits)
    p = GetPrime.getPrime(bits)
    q = GetPrime.getPrime(bits)

    return generateKey(p, q)