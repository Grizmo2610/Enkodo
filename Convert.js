function encode(input) {
    const message = input.toString();
    return btoa(message);
}

function encodeBase64(data) {
    result = [];
    for (const number of data) {
        result.push(encode(number.toString()));
    }
    return result;
}

function convertToDemical(data) {
    const encodedBase64 = data.trim()
    return atob(encodedBase64);
}

function decodeBase64(data) {
    let result = [];
    try {
        for (const i of data) {
            if (i != "") {
                result.push(BigInt(convertToDemical(i)))
            };
        }
    } catch (error) {
        alert("Not a suitable base64 data!")
    }

    return result;
}