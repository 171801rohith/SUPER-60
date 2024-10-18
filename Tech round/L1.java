import java.util.Scanner;

/**
 * L1_2
 */
public class L1 {

    static int conNeg(int num) {
        return -num;
    }

    public static void main(String[] args) {
        int rem, num;
        int i = 0;
        int[] a = new int[2];
        int[] nine = new int[101];
        for (i = 0; i < 101; i++) {
            nine[i] = 9 * i;
        }
        for (i = 0; i < 101; i++) {
            num = nine[i];
            int j = 0;
            while (j < 2) {
                rem = num % 10;
                num = num / 10;
                a[j] = rem;
                j++;
            }
            if (a[0] - a[1] == 3 || a[0] - a[1] == -3) {
                nine[i] = nine[i] * -1;
            } else {
                nine[i] = nine[i];
            }
        }

        System.out.println();
        for (i = 0; i < 101; i++) {
            System.out.print(nine[i] + ", ");
        }
        int sum = 0;
        System.out.println();
        for (i = 0; i < 101; i++) {
            sum += nine[i];
        }
        System.out.println("Sum="+sum);
    }
}