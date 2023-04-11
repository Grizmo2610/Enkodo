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

def crypt(text: list[int]) -> str:
    """
    The provided function takes a list of integers text as input and returns a string containing 
    the integers separated by spaces.

    The function first applies the map function to the text list, which applies the str function to
    each integer in the list, converting them to strings.

    The resulting list of strings is then passed to the join method of the string " ", which joins 
    the strings together with spaces as separators.

    Parameter:
        text (list[int]): list of integers

    Return (str): the resulting string.
    """
    return ' '.join(list(map(str, text)))


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
            f.write("".join(text[i]))
            if i != len(text) - 1:
                f.write("\n")
