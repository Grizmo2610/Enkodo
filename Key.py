from os import makedirs
import json
from random import randint
import random


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

def isPrime(n: int, k : int = 30):
	"""
	This function check if number is a prime number or not
	Parameters:
		number (int):  A integet Number need to check

	Return: (boolean) - True if number is a prime number and false if not
	"""
	if n < 2:
		return False
	for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
		if n % p == 0:
			return n == p
		

	s, d = 0, n - 1
	while d % 2 == 0:
		s, d = s + 1, d // 2
	for _ in range(k):
		a = randint(2, n - 2)
		x = pow(a, d, n)
		if x != 1 and x != n - 1:
			for i in range(s - 1):
				x = pow(x, 2, n)
				if x != n - 1 and i == s - 2:
					return False
	return True

def nextPrime(number: int):
	"""
	This function find nearest prime number with number biger than.
	If function is an even number, then number = number + 1. number = number + 2 until number is a prime number.

	"""
	if number % 2 == 0:
		number += 1
	while not isPrime(number):
		number += 2
	return number

def randomNumber (bits: int = 1024):
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

def generateKey(p: int, q: int):
	"""
	This function generate pair of key ((e, n), (n, d)) using RSA Algorithm.
	Caculate:
		Euler:
			euler = (p - 1) * (q - 1).
		n: 
			n = p * q
		Carmichael: 
			Least Common Multiple
		e: 
			An random integer between 1 and Carmichael which Have greatest common divisor with euler is 1
		d:
			d = 1 / e mod carmichael

	Parameters:
		p (int): A prime number
		q (int): A prime number

	Return: tuple(tuple(int, int), tuple(int, int)) - pair of key (public key, private key)
	"""
	
	p = nextPrime(p)
	q = nextPrime(q)

	euler = (p - 1) * (q - 1)
	carmichael = euler // gcd(p - 1, q - 1)

	e = randint(2, carmichael - 1)
	while gcd(e, euler) != 1:
		e = randint(2, carmichael - 1)

	return (e, p * q), (p * q, pow(e, -1, carmichael))


def randomKey(bits: int = 1024):
	"""
	This method generate random key with pair p, q have length of bits

	Parameter:
		bits (int): an integer number
	
	Return: tuple(tuple(int, int), tuple(int, int)) - pair of key (public key, private key)
	"""
	p = nextPrime(randomNumber(bits))
	q = nextPrime(randomNumber(bits))

	print(isPrime(p), isPrime(q))
	with open("data\PrimeNumber.txt", 'w') as f:
		f.write(str(p) + '\n')
		f.write(str(q))

	return generateKey(p, q)


def saveKey(publicKey: tuple[int], privateKey: tuple[int]) -> None:
	"""
	This function takes two tuples, publicKey and privateKey, and saves them as a JSON file
	named key.json in a subdirectory named data.

	The makedirs function is called with the argument 'data' to create the data subdirectory 
	if it does not exist already. The exist_ok=True argument is used to avoid raising an exception
	if the directory already exists.

	The open function is then used to open the key.json file in write mode with the 'w' argument. 
	The json.dump function is then called with a dictionary containing the n, e, and d values of 
	the publicKey and privateKey tuples. This dictionary is written to the key.json file in JSON format.

	Parameters:
		publicKey (tuple(int)): public key using to encrypt
		privateKey (tuple(int)): private key using to decrypt


	"""
	makedirs('data', exist_ok=True)
	with open('data\key.json', 'w') as f:
		json.dump(
			{"n": publicKey[1], "e": publicKey[0], "d": privateKey[1]}, f)


def getKey(path: str) -> tuple[tuple[int, int], tuple[int, int]]:
	"""
	This function takes a file path as input and returns two tuples representing the public and 
	private keys for RSA encryption.
	It opens the file at the specified path in read mode then reads the contents of the file as a 
	string. Uses the json.loads() method to convert the string to a Python dictionary.

	It extracts the values for the n, e, and d keys from the dictionary using dict.values() method 
	and creates two tuples: one containing the (e, n) values for the public key, and another 
	containing the (n, d) values for the private key.

	Parameters:
		path (str): path to file need to read

	Return: (tuple[tuple[int, int], tuple[int, int]]) - these two tuples.
	"""
	with open(path, 'r') as file:
		data = file.read()

	# Convert JSON to python List
	n, e, d = list(dict(json.loads(data)).values())
	return (e, n), (n, d)
