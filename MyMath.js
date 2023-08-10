function gcd(a, b) {
    a = BigInt(a)
    b = BigInt(b)
    // Tính ước chung lớn nhất (GCD) của hai số a và b
    while (b !== BigInt(0)) {
        const temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

function modInverse(a, m) {
    a = BigInt(a)
    m = BigInt(m)

    // Tìm nghịch đảo modulo của a trong mod m
    let m0 = m;
    let x0 = BigInt(0);
    let x1 = BigInt(1);

    if (m === 1) {
        return 1;
    }

    while (a > 1) {
        const q =(a / m) / BigInt(1);
        let t = m;

        m = a % m;
        a = t;
        t = x0;
        x0 = x1 - q * x0;
        x1 = t;
    }

    if (x1 < BigInt(0)) {
        x1 += m0;
    }

    return x1;  
}

// Hàm tính lũy thừa modulo
function powerMod(base, exponent, modulus) {
    base = BigInt(base)
    exponent = BigInt(exponent)
    modulus = BigInt(modulus)

    if (modulus === BigInt(1)) 
        return BigInt(0);

    let result = BigInt(1);
    base = base % modulus;
    while (exponent > BigInt(0)) {
        if (exponent % BigInt(2) === BigInt(1)) {
            result = (result * base) % modulus;
        }
        exponent = (exponent / BigInt(2)) / BigInt(1);
        base = (base * base) % modulus;
    }
    return result;
}

function getRandomIntBetween(a, b) {
    a = BigInt(a)
    const timeSeed = new Date().getTime(); // Lấy thời gian hiện tại
    const randomSeed = (timeSeed % (b - a + BigInt(1))) + a;

    return randomSeed;
}