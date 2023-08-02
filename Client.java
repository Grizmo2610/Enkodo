import java.util.Arrays;
import java.util.Scanner;

public class Client {
    static Scanner input = new Scanner(System.in);
    public static String inputMessage(){
        return input.next();
    }

    public static int inputBits(){
        int bits = 0;
        while (bits < 8){
            bits = input.nextInt();
        }
        return bits;
    }

    public static int[][] inputKey(){
        int[][] key;
        if (input.next().equals("Custom")){
            int p = inputPrimeNumber();
            int q = inputPrimeNumber();
            return Key.customKey(p, q);
        }
        int bits = inputBits();
        return Key.randomKey(bits);

    }

    public static int[] inputCipher(){
        return new int[0];
    }

    public static int inputPrimeNumber(){
        int number = 0;
        while (PrimeTest.checkPrime(number)){
            number = input.nextInt();
        }
        return number;
    }

    public static void main(String[] args) {
        String inputVar = input.next(); // Lựa chọn người dùng

        if (inputVar.equals("Encrypt")){ // Nếu chọn mã hóa
            String message = inputMessage();

            // Tạo khóa
            int[][] key = inputKey();
            int[] publicKey = key[0];
            int[] privateKey = key[1];

            int[] result = Encrypt.encoding(message, publicKey); // Đoạn mã dược mã hóa

            System.out.println("Public key: " + Arrays.toString(publicKey));
            System.out.println("Private key: " + Arrays.toString(privateKey));
            System.out.println(Arrays.toString(result)); // Đưa ra kết quả

        } else if (inputVar.equals("Decrypt")){
            int[] cipher = inputCipher();
            // Tạo khóa
            int[][] key = inputKey();
            int[] publicKey = key[0];
            int[] privateKey = key[1];

            String result = Decrypt.decrypt(cipher, privateKey);
            System.out.println(result); // Đưa ra kết quả
        }

    }
}
