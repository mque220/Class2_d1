import java.util.Scanner;

public class Hashing {
    public static final int M = 1234567891;
    public static final int r = 31;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int len = Integer.parseInt(sc.nextLine());
        long m = 1;
        long H = 0;
        char[] arr = sc.nextLine().toCharArray();
        for (int i = 0; i < len; i++) {
            int num = (byte)arr[i] - 96;
            H = (H + (num * m % M)) % M;
            m = (m * r) % M;
        }
        System.out.println(H);
        sc.close();
    }
}