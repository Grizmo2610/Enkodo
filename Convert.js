function encode(input) {
    const message = input.toString();
    const utf8Encoder = new TextEncoder();
    const data = utf8Encoder.encode(message);
    return btoa(String.fromCharCode(...data));
}

function encodeBase64(data) {
    result = [];
    for (const number of data) {
        result.push(encode(number.toString()));
    }
    return result;
}

function convertToDemical(data) {
    // Chuyển đổi chuỗi Base64 về Uint8Array (mảng các byte)
    alert(data)
    const decodedData = new Uint8Array(atob(data).split('').map(char => char.charCodeAt(0)));
    // Chuyển Uint8Array thành chuỗi gốc
    const utf8Decoder = new TextDecoder();
    return utf8Decoder.decode(decodedData);
}

function decodeBase64(data) {
    let result = [];
    for (const i of data){
        result.push(BigInt(convertToDemical(i)));
    }
    return result;
}