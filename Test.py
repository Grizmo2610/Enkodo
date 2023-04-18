import Decrypt
import Encrypt
import Key
import FindingKey
import time

if __name__ == "__main__":
    p = 163799160197134459132100397031692924582140521143395065308165662909921731475492881461885714198763447790540722189270461047716065749053243729458406978243702676245271139995501580688628076737625444142578429466339861368858551501197567226430703695824931148294023468989931292056209256389858704308853423367966743482191
    q = 149303830103537302718331149637557961636628297749789399546261072665768777045020575638219088388062299505276053863200809202577104436887509450785219783246599794655893290094438596385699374460820733662284252500585022896903027767819107178048857396922447758961077716916382851972496676264274467387771873501935840755741
    
    start = time.time()
    # Generate pair of key
    # publicKey, privateKey = Key.randomKey()
    publicKey, privateKey = Key.generateKey(p, q)

    print('Generate key time:', time.time() - start)
    print("Pair of key:", (publicKey, privateKey ))

    # message
    msg = ""
    with open('data\PlainText.txt') as f:
        msg = f.read()

    start = time.time()
    # Encrypt message
    cipherText = Encrypt.encoding(msg, publicKey)
    print('Encrypt time:', time.time() - start)

    with open('data\out.txt', 'w') as f:
        msg = f.write('\n'.join(Encrypt.crypt(cipherText)))

    Encrypt.saveData(cipherText)

    # Save key
    Key.saveKey(publicKey, privateKey)

    # Get key
    # print('Pair of key from file:', Key.getKey('data\key.json'))

    start = time.time()
    # Decrypt cipher text
    plainText = Decrypt.decypt(cipherText, privateKey)

    print('Decrypt time:', time.time() - start)

    # Print plaintext
    print('Plain text:\n' + plainText)

    # Find private key with public key
    # print('Private key:', FindingKey.findPrivateKey(publicKey))
