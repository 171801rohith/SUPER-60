// Problem Statement
// Level 1: Generate and Modify a Sequence
// 1. Generate an array of 100 integers based on the below series:
//     1 2 5 10 17 26 37 50 65 82 101... (100 such numbers)
// 2. If the number in the series ends with an even number, change that number to its negative form. 
//     Example: 2 becomes -32.  10 becomes -10. Another example: 26 becomes -26. 
// 3. Display the final array with all 100 modified numbers. 
// 4. Display the sum of all these 100 numbers. 

// Level 2: Numbers with 0 (zero) as a digit
// 1. From the array generated in Level 1, identify all numbers which contain 0 (zero) as one of the digits.  
//      Ex: 10, 50, 101
// 2. Display all such numbers that meet this criterion. 
// 3. Find and display the sum of all these numbers. 

// Level 3: Ascending digit numbers
// 1. From the array generated in Level 1, identify and display all the numbers which contain digits
// in the ascending order. Ex: 17, -26, 37, 145, 257
// 2. Display all such numbers that meet this criterion. 
// 3. Find and display the sum of all these numbers.

import java.util.ArrayList;

public class LAB2 {
    public static void display(int[] array) {
        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i] + " ");
        }
    }

    public static int checkEven(int num) {
        if (num % 2 == 0) {
            return (num * -1);
        }
        return num;
    }

    public static void sumArr(int[] array) {
        double sum = 0;
        for (int i = 0; i < array.length; i++) {
            sum += array[i];
        }
        System.out.println("Sum of the array is " + sum);
    }

    public static boolean containsZero(int num) {
        int digit;
        while (num > 0) {
            digit = num % 10;
            num /= 10;
            if (digit == 0) {
                return true;
            }
        }
        return false;
    }

    public static void sumArr(ArrayList<Integer> aList) {
        double sum = 0;
        for (int i = 0; i < aList.size(); i++) {
            sum += aList.get(i);
        }
        System.out.println("Sum of the array is " + sum);
    }

    public static boolean checkOrder(int num) {
        ArrayList<Integer> list = new ArrayList<>();
        while (num > 0) {
            list.add(num % 10);
            num /= 10;
        }
        for (int i = 0; i < list.size() - 1; i++) {
            if (list.get(i) < list.get(i + 1) || list.get(i) == list.get(i + 1)) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        int[] arr = new int[100];
        arr[0] = 1;
        for (int i = 1, j = 0; i < arr.length; i++, j++) {
            arr[i] = arr[i - 1] + (2 * j) + 1;
        }

        display(arr);
        System.out.println();
        System.out.println();

        for (int i = 0; i < arr.length; i++) {
            arr[i] = checkEven(arr[i]);
        }

        display(arr);
        System.out.println();
        System.out.println();

        sumArr(arr);
        System.out.println();
        System.out.println();

        ArrayList<Integer> zeroArr = new ArrayList<>();
        for (int i = 0; i < arr.length; i++) {
            if (containsZero(Math.abs(arr[i]))) {
                zeroArr.add(arr[i]);
            }
        }

        System.out.println(zeroArr);
        System.out.println();
        System.out.println();

        sumArr(zeroArr);
        System.out.println();
        System.out.println();

        ArrayList<Integer> orderArr = new ArrayList<>();
        for (int i = 0; i < arr.length; i++) {
            if (checkOrder(Math.abs(arr[i]))) {
                orderArr.add(arr[i]);
            }
        }

        System.out.println(orderArr);
        System.out.println();
        System.out.println();

        sumArr(orderArr);
        System.out.println();
        System.out.println();
    }
}
