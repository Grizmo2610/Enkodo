import Key


def primeFactor(number: int) -> tuple[int]:
    """
    The primeFactor function takes an integer number as input and returns a list of prime factors of number.

    The function first checks if the number is divisible by 2 and adds 2 to the list of factors if 
    it is not already in the list. Then, it checks for odd divisors from 3 to half of the number 
    (using range(3, number // 2 + 1, 2) to iterate over odd numbers only), and adds them to the 
    factor list if they divide the number evenly. It divides the number by each divisor as many 
    times as possible before moving on to the next one. Finally, it returns the list of prime factors.

    Parameter:
        number (int): An integer number

    Return: (list[int]) - all prime number factor of number
    """
    factor = []
    while number % 2 == 0:
        number /= 2
        if 2 not in factor:
            factor.append(2)

    for divisor in range(3, number // 2 + 1, 2):
        while number % divisor == 0:
            number /= divisor
            if divisor not in factor:
                factor.append(divisor)
    return factor


def findPrivateKey(publicKey: tuple[int]) -> tuple[int, int]:
    """
    The findPrivateKey function takes a publicKey tuple (e, n) as input and returns the 
    corresponding private key (n, d), where d is the modular multiplicative inverse of e modulo 
    the Carmichael's totient function of n.

    The factor variable is assigned to the list of prime factors of n. If n doesn't have exactly 
    two prime factors, the function returns None. Otherwise, p and q are assigned to the two prime factors.

    The Euler totient function of n is computed by multiplying p-1 and q-1. The Carmichael's totient 
    function of n is computed by dividing the Euler totient by the greatest common divisor of p-1 
    and q-1. The pow function is used to compute the modular multiplicative inverse of e modulo the 
    Carmichael's totient function of n.

    Parameters:
        publicKey (list[int]): public key to Encrypy

    Return: (tuple[int, int]) - private key
    """
    e, n = publicKey
    factor = primeFactor(n)
    p, q = factor
    euler = (p - 1) * (q - 1)
    carmichael = euler // Key.gcd(p - 1, q - 1)
    return (n, pow(e, -1, carmichael))
