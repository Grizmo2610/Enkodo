public class Key {

    /***
     * Tạo key
     * key[0] = public key
     * key[1] = private key
     *
     * @param p số nguyên tố
     * @param q số nguyên tố
     * @return Cặp khóa
     */
    public static int[][] customKey(int p, int q){
        int[][] key = new int[2][2];

        int n, d, e;
        n = 0;
        d= 0;
        e = 0;

        // Tạo khóa ở đây
        key[0] = new int[]{e, n};
        key[1] = new int[]{n, d};
        return key;
    }

    /**
     * Tạo khóa ngẫu nhiên bằng cách tạo ngẫu nhiên 2 số nguyên tố p và q
     * sau đó gọi đến phương thức customKey và truyền 2 tham số p và q vào
     * */
    public static int[][] randomKey(int bits){
        int p = GetPrimeNumber.getPrime(bits);
        int q = GetPrimeNumber.getPrime(bits);
        return customKey(p,q);
    }
}
