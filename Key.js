function generateRSAKeyPair(size) {
    const p = getPrime(size)
    const q = getPrime(size)

    const euler = (p - 1) * (q - 1);
    const carmichael = euler / gcd(p - 1, q - 1);

    const n = p * q;
    let e = 65537;
    while (gcd(e, carmichael) !== 1) {
        e = Math.floor(Math.random() * (carmichael - 2)) + 2;
    }

    const d = modInverse(e, euler);
    publicKey = {
        n: n,
        e: e
    };
    privateKey = {
        n: n,
        d: d
    };
}