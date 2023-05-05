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

def isPrime(number: int) -> bool:
    """
    This method takes an integer input number and returns True if number is a prime number and False 
    if number is not a prime number.
    
    Parameter:
			number (int): an integer
    
    Returns: (bool) - number is a prime number or not
    """
    return PrimeTest.Preprocessor(number) and PrimeTest.fermat(number, 20) and PrimeTest.millerRabin(number, 20)


def getPrime(bits: int = 1024) -> int:
    """
    This method is used to generate a random prime number with the length of `bits`
    
    Parameter:
        	bits (int): An integer number

    Return: (int) - random prime number with the length of bits
    """
    number = randomNumber(bits)
    while not isPrime(number):
        number += 2
    return number


def savePrime(p: int, q: int) -> None:
    """
    This method is uesd to save two prime number into data\PrimeNumber.txt
    
    Parameter:
		p (int): first prime number
        q (int): first prime number
        
    Return: None
    """
    with open("data\PrimeNumber.txt", 'w') as f:
        f.write(str(p) + '\n')
        f.write(str(q))
