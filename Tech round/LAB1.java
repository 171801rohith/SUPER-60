// Problem Statement

// Level 1: Generate and Modify a Sequence
// 1. Generate an array of 100 integers where each number is a multiple of 9, starting from 9 (i.e., 9, 18, 27, 36,...). 
// 2. For each number, if the difference between its last two digits is 3, change that number to its negative form. 
//     Example:  36 has last two digits 3 and 6, the difference is 3, so it becomes -36. 63 has last two digits 6 and 3, the difference is 3, so it becomes -63. 
// 3. Display the final array with all 100 modified numbers. 
// 4. Display the sum of all these 100 numbers. 

// Level 2: Numbers with Prime Neighbors
// 1. From the array generated in Level 1, identify all numbers n where either n-1 or n+1 is a prime number. 
// 2. Display all such numbers that meet this criterion. 
// 3. Find and display the sum of all these numbers. 

// Level 3: Ascending Subarrays
// 1. From the array generated in Level 1, identify and display all subarrays where the numbers are in strictly ascending order. 
// 2. For each such subarray, calculate the sum of its elements. 
// 3. Display the sum of all these individual subarray sums. 
// 4. Display the number of subarrays. 
// 5. Finally, calculate and display the total sum of all the sums of the ascending subarrays.

import java.util.ArrayList;

public class LAB1 {
    public static void display(int[] array) {
        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i] + " ");
        }
    }

    public static int checkDiff(int num) {
        int n = num;
        int[] last2digis = new int[2];
        for (int i = 0; (i < 2 && n > 0); i++) {
            last2digis[i] = n % 10;
            n /= 10;
        }
        if (Math.abs(last2digis[0] - last2digis[1]) == 3) {
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

    public static void sumArr(ArrayList<Integer> aList) {
        double sum = 0;
        for (int i = 0; i < aList.size(); i++) {
            sum += aList.get(i);
        }
        System.out.println("Sum of the array is " + sum);
    }

    public static boolean isPrime(int n) {
        int count = 0;
        for (int i = 1; i <= n; i++) {
            if (n % i == 0) {
                count++;
            }
        }
        if (count > 2) {
            return false;
        }
        return true;
    }

    public static void main(String[] args) {
        int[] arr = new int[101];
        for (int i = 1; i < arr.length; i++) {
            arr[i - 1] = 9 * i;
        }

        display(arr);
        System.out.println();
        System.out.println();
        for (int i = 0; i < arr.length; i++) {
            arr[i] = checkDiff(arr[i]);
        }

        display(arr);
        System.out.println();
        System.out.println();

        sumArr(arr);
        System.out.println();
        System.out.println();

        ArrayList<Integer> primeArr = new ArrayList<>();
        for (int i = 1; i < arr.length - 1; i++) {
            if (isPrime(Math.abs(arr[i]) - 1) || isPrime(Math.abs(arr[i]) + 1)) {
                primeArr.add(arr[i]);
            }
        }

        System.out.println(primeArr);
        System.out.println();
        System.out.println();
        
        sumArr(primeArr);
        System.out.println();
        System.out.println();

        

    }
}
