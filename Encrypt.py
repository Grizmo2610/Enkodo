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