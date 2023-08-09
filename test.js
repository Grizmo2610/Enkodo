import BigInteger from './node_modules/big-integer/BigInteger.js';

const a = new BigInteger(123456789);
const b = new BigInteger('987654321');

const sum = a.add(b);
alert(sum.toString()); // Kết quả: 1111111110