import Key

def decypt(cipherText: list[int], privateKey: tuple[int] = ...) -> str:
    """
    This function takes in a list of cipher text and a private key as input and 
    returns the decrypted message as a string.

    Parameter: 
        cipherText (list[int]): list of cipher text
        privateKey tuple[int]: a pair of number (n, d) 0 private key 

    Return: (str) - the decrypted message as a single string.
    """    
    n, d = privateKey
    if privateKey == ...:
        try:
            publicKey, (n, d)= Key.getKey('data\key.json')
        except:
            print("No Private key")
            return None


    result = []
    for char in cipherText:
        result.append(chr(pow(char, d, n)))
    return ''.join(result)