import Key
from os import makedirs


def encoding(message: str, publicKey: tuple[int] = ...) -> list[int]:
    """
    This function takes a message string and an optional publicKey tuple as input and 
    returns a list of integers representing the encrypted message.

    Parameters:
        publicKey (tuple(int)): public key using to encrypt
        privateKey (tuple(int)): private key using to decrypt

    Return list[int]: list of integers representing the encrypted message.
    """
    if publicKey == ...:
        publicKey, privateKey= Key.randomKey()

    (e, n) = publicKey
    return [pow(ord(char), e, n) for char in message]

def toText(number: int):
    """
    This function convert an integer number in to a string

    Parameters:
        number (int): an integer to convert
    
    Return: str - text have been converted
    """
    result = ""
    s = str(number)
    for i in range(0, len(s), 3):
        num = int(s[i:i+3])
        if num >= 127 or num < 35:
            result += '\\{:03d}'.format(num)
        else:
            result += chr(num)   
    return result

def crypt(text:list[int]):
    """
    This function convert all element in a list to a text

    Parameters:
        text (list[int]): list number to convert

    Return: list[str] - list have converted
    """
    result = []
    for i in text:
        result.append(toText(i))
    return result

def saveData(text: list[int]) -> None:
    """
    This function is used takes a list of integers text as input and saves it as a text file named 
    ciphertext.txt in a subdirectory named data.

    Parameters list[int]: a list of integers

    Return: None
    """

    makedirs('data', exist_ok=True)

    with open('data\ciphertext.txt' , "w", encoding= "utf-8") as f:
        for i in range(len(text)):
            f.write(str(text[i]))
            if i != len(text) - 1:
                f.write("\n")