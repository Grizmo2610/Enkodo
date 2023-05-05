import Decrypt
import Encrypt
import Key
import time

if __name__ == "__main__":
    start = time.time()
    # Generate pair of key
    publicKey, privateKey = Key.randomKey(1024)
    print('Generate key time:', time.time() - start)

    # message
    msg = ""
    with open('data\PlainText.txt') as f:
        msg = f.read()

    start = time.time()
    # Encrypt message
    cipher = Encrypt.encoding(msg, publicKey)
    print('Encrypt time:', time.time() - start)

    Encrypt.saveData(cipher)

    # Save key
    Key.saveKey(publicKey, privateKey)

    # Decrypt cipher text
    start = time.time()
    plainText = Decrypt.decypt(cipher, privateKey)
    print('Decrypt time:', time.time() - start)

    # Print plaintext
    print('Plain text:\n' + plainText)