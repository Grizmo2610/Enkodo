public class GetPrimeNumber {
    /***
     * Số ngẫu nhiên có độ dài bits
     * @param bits độ dài bits
     * @return số ngẫu nhiên
     */
    private static int randomNumber(int bits){
        return 5;
    }

    /***
     * Lấy số nguyên tố lớn hơn hoặc bằng số được truyền vào
     *
     * @param number một số nguyên
     * @return số nguyên tố
     */

    private static int nextPrime(int number){
        if (PrimeTest.checkPrime(number))
            // Nếu số chuyền vào đã nguyên tố thì trả về chính nó
            return number;

        // Nếu là số chia hết cho 2 thì + 1 để lúc sau +2 giảm bớt thời gian
        if (number % 2 == 0){
            number += 1;
        }

        while (PrimeTest.checkPrime(number))
            number += 2;
        return number;
    }

    /***
     *
     *
     * @param bits độ dài bits
     * @return số nguyên tố có độ dài bits
     */
    public static int getPrime(int bits){
        int result = randomNumber(bits);
        result = nextPrime(result);
        return result;
    }
}
