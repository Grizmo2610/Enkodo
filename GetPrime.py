import random
import PrimeTest


def randomNumber(bits: int = 1024):
    """
    This method is used to generate a random integer with the length of 'bits'
    Parameter:
            bits (int): An integer number

    Return: (int) - random integer
    """
    number = random.getrandbits(bits)
    number = number | (1 << (bits-1))
    number = number | 1
    return number


def nextPrime(number: int):
    """
    This function take an number and return a prime number which nearest and bigger than number

    Parameter: 
        number (int): - an integer number

    Return (int): - a prime number
    """

    while not PrimeTest.isPrime(number):
        number += 2
    return number

def getPrime(bits: int = 1024) -> int:
    """
    This method is used to generate a random prime number with the length of `bits`
    
    Parameter:
        	bits (int): An integer number

    Return: (int) - random prime number with the length of bits
    """
    number = randomNumber(bits)

    return nextPrime(number)