import Key
from os import makedirs


def encoding(message: str, publicKey: tuple[int] = ...) -> list[int]:
    """
    The provided function takes a message string and an optional publicKey tuple as input and 
    returns a list of integers representing the encrypted message.

    If no publicKey is provided, the randomKey() method of a Key object is called to generate a 
    random public key, as well as values for e and n.

    The publicKey tuple is then unpacked into the e and n variables.

    The function then uses a list comprehension to iterate over each character i in the message 
    string and applies the RSA encryption formula pow(ord(i), e, n) to obtain the encrypted integer
    representation of the character. The ord() function returns the ASCII code of the character,
    which is used as the input to the encryption formula.


    Parameters:
        publicKey (tuple(int)): public key using to encrypt
        privateKey (tuple(int)): private key using to decrypt

    Return list[int]: list of integers representing the encrypted message.
    """
    e, n = 0, 0
    if publicKey == ...:
        publicKey, privateKey= Key.randomKey()

    (e, n) = publicKey

    return [pow(ord(i), e, n) for i in message]

def toText(number: int):
    """
    This method convert an integer number in to a string

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
    This method convert all element in a list to a text

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
    The provided function takes a list of integers text as input and saves it as a text file named 
    ciphertext.txt in a subdirectory named data.

    The makedirs function is called with the argument 'data' to create the data subdirectory if it 
    does not exist already. The exist_ok=True argument is used to avoid raising an exception if the
    directory already exists.

    The open function is then used to open the ciphertext.txt file in write mode with the 'w' 
    argument and the encoding parameter set to "utf-8".

    The function then iterates over each integer i in the text list and writes it to the file as a 
    string  using the write method of the file object. It also writes a newline character after 
    each integer, except for the last one.

    Parameters list[int]: a list of integers
    """

    makedirs('data', exist_ok=True)

    with open('data\ciphertext.txt' , "w", encoding= "utf-8") as f:
        for i in range(len(text)):
            f.write(str(text[i]))
            if i != len(text) - 1:
                f.write("\n")
