from os import makedirs
import json
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

    d = pow(e, -1, euler)
    return (e, n), (n, d)


def randomKey(bits: int = 1024):
    """
    This method generate random key with pair p, q have length of bits

    Parameter:
            bits (int): an integer number

    Return: tuple(tuple(int, int), tuple(int, int)) - pair of key (public key, private key)
    """
    p = GetPrime.getPrime(bits)
    q = GetPrime.getPrime(bits)

    GetPrime.savePrime(p, q)

    return generateKey(p, q)


def saveKey(publicKey: tuple[int], privateKey: tuple[int]) -> None:
    """
    This function takes two tuples, publicKey and privateKey, and saves 
    them as a JSON file named key.json in a subdirectory named data.

    Parameters:
            publicKey (tuple(int)): public key using to encrypt
            privateKey (tuple(int)): private key using to decrypt

    Return: None
    """
    makedirs('data', exist_ok=True)
    with open('data\key.json', 'w') as f:
        json.dump(
            {"n": publicKey[1],
             "e": publicKey[0],
             "d": privateKey[1]}, f)


def getKey(path: str) -> tuple[tuple[int, int], tuple[int, int]]:
    """
    This function takes a file path as input and returns two tuples 
    representing the public and private keys for RSA encryption.

    Parameters:
            path (str): path to file need to read

    Return: (tuple[tuple[int, int], tuple[int, int]]) - these two tuples.
    """
    with open(path, 'r') as file:
        data = file.read()

    # Convert JSON to python List
    n, e, d = list(dict(json.loads(data)).values())
    return (e, n), (n, d)