// -------Hàm chạy chương trình--------------//
let publicKey, privateKey;

// Hàm xử lý khi người dùng nhấn nút Generate Keys
function generateKeys() {
  const keySize = Number(document.getElementById('keySize').value);
  generateRSAKeyPair(keySize);
  document.getElementById('npublic').value = publicKey.n;
  document.getElementById('e').value = publicKey.e;
  document.getElementById('nprivate').value = privateKey.n;
  document.getElementById('d').value = privateKey.d;
}

function publicKeys() {
  publicKey = {
    n: document.getElementById('npublic').value,
    e: document.getElementById('e').value
  };
}

function privateKeys() {
  privateKey = {
    n: BigInt(document.getElementById('nprivate').value),
    d: BigInt(document.getElementById('d').value)
  };
}

function getKeys() {
  publicKeys();
  privateKeys();
}

// Hàm mã hóa dữ liệu sử dụng khóa công khai RSA
function encrypt(publicKey, data) {
  const e = publicKey.e,
    n = publicKey.n;
  const encryptedData = data.split('').map(char => powerMod(BigInt(char.charCodeAt(0)), BigInt(e), BigInt(n)));
  return encryptedData;
}

// Hàm xử lý khi người dùng nhấn nút Encrypt Data
function encryptData() {
  if (document.getElementById('npublic').value === "" && document.getElementById('e').value === "") {
    generateKeys();
  } else {
    getKeys();
  }
  const inputData = document.getElementById('inputData').value;
  encryptedData = encrypt(publicKey, inputData);
  document.getElementById('outputString').value = encodeBase64(encryptedData).join('\n');

  // Tự động kéo xuống khi bấm nút
  const resultDiv = document.getElementById("outputString");
  resultDiv.scrollIntoView({
    behavior: "smooth"
  });
}

// Hàm giải mã RSA
function decrypt(encryptedData, key) {
  const d = key.d;
  const n = key.n;
  const result = [];
  try {
    for (const char of encryptedData) {
      result.push(String.fromCharCode(Number(powerMod(char, d, n))));
    }
    return result;
  } catch (error) {
    alert("Private key may not be suitable for this data!");
  }
}

// Hàm xử lý khi người dùng nhấn nút Decrypt Data
function decryptData() {
  privateKeys();
  encryptedData = (document.getElementById('inputData').value).split("\n");
  if (privateKey.n === "" || privateKey.d === "" || encryptedData === "") {
    alert("Required fields missing.");
  } else {
    if (isBase64(encryptedData)) {
      encryptedData = decodeBase64(encryptedData);
    }
    let decryptedData = decrypt(encryptedData, privateKey);
    document.getElementById('outputString').value = decryptedData.join("");
  }

  // Tự động kéo xuống khi bấm nút
  const resultDiv = document.getElementById("outputString");
  resultDiv.scrollIntoView({
    behavior: "smooth"
  });
}

function isBase64(inputString) {
  return (/[a-zA-Z]/.test(inputString) && /\d/.test(inputString)) || /[a-zA-Z]/.test(inputString);
}