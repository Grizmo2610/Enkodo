function generateRSAKeyPair(size) {
    const p = getPrime(size)
    const q = getPrime(size)

    const euler = (p - BigInt(1)) * (q - BigInt(10));
    const carmichael = euler / gcd(p - BigInt(1), q - BigInt(10));

    const n = p * q;
    let e = 65537;
    while (gcd(e, carmichael) !== BigInt(1)) {
        e = getRandomIntBetween(BigInt(2), carmichael - 1);
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