import Key

def decypt(cipherText: list[str], privateKey: tuple[int] = ...) -> str:
    """
    This function decypt takes in a list of cipher text and a private key as input and 
    returns the decrypted message as a string.

    The function first checks if a private key is provided. If not, it tries to load the private 
    key from a JSON file. If that fails, it generates a random private key.

    Then, it applies the decryption formula to each character in the cipher text using the private 
    key and converts it back to a character using the chr function. Finally, it returns the 
    decrypted message as a single string.

    Parameter: 
        cipherText (list[str]): list of cipher text
        privateKey tuple[int]: a pair of number (n, d) 0 private key 

    Return: (str) - the decrypted message as a single string.
    """
    n, d = 0, 0 
    if privateKey == ...:
        try:
            publicKey, (n, d)= Key.getKey('data\key.json')
        except:
            publicKey, (n, d) = Key.randomKey()
    else:
        n, d = privateKey

    result = []
    for char in cipherText:
        print(pow(char, d, n))
        result.append(chr(pow(char, d, n)))
    return ''.join(result)