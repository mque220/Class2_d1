import java.util.Scanner;
import java.util.ArrayList;

public class Hotel {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int input_num = Integer.parseInt(sc.nextLine());

        ArrayList<Integer> results = new ArrayList<>();
        for (int i = 0; i < input_num; i++) {
            String[] array = sc.nextLine().split(" ");
            int H = Integer.parseInt(array[0]);
            int N = Integer.parseInt(array[2]);
            int room_num = 0;
            for (int j = 0; j < N; j++) {
                if (j % H == 0) {
                    room_num = (room_num % 100) + 1;
                }
                room_num += 100;
            }
            results.add(room_num);
        }
        
        for (int i = 0; i < results.size(); i++) {
            System.out.println(results.get(i));
        }
        
        sc.close();
    }
}
