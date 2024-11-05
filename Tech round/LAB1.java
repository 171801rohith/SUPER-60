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

    public static double sumArr(int[] array) {
        double sum = 0;
        for (int i = 0; i < array.length; i++) {
            sum += array[i];
        }
        return sum;
    }

    public static double sumArr(double[] array) {
        double sum = 0;
        for (int i = 0; i < array.length; i++) {
            sum += array[i];
        }
        return sum;
    }

    public static double sumArr(ArrayList<Integer> aList) {
        double sum = 0;
        for (int i = 0; i < aList.size(); i++) {
            sum += aList.get(i);
        }
        return sum;
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

    public static void Level_3(int[] arr) {
        ArrayList<ArrayList<Integer>> finalArr = new ArrayList<>();
        for (int i = 0; i < arr.length; i++) {
            ArrayList<Integer> subArr = new ArrayList<>();
            subArr.add(arr[i]);
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[j] > 0) {
                    subArr.add(arr[j]);
                } else {
                    finalArr.add(subArr);
                    i = j - 1;
                    break;
                }
            }
        }

        double[] sumArray = new double[finalArr.size()];

        int i = 0;
        for (ArrayList<Integer> row : finalArr) {
            System.out.format("SubArray[%2d] = ", i + 1);
            sumArray[i] = sumArr(row);
            System.out.println(row);
            System.out.println("SUM = " + sumArray[i]);
            System.out.println();
            i++;
        }
        System.out.println("Number of SubArrays = " + finalArr.size());
        System.out.println();
        System.out.println("Sum = " + sumArr(sumArray));
        System.out.println();
        System.out.println();
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

        System.out.println("Sum of Array = " + sumArr(arr));
        System.out.println();
        System.out.println();

        ArrayList<Integer> primeArr = new ArrayList<>();
        for (int i = 1; i < arr.length - 1; i++) {
            if (arr[i] < 0) {
                continue;
            }
            if (isPrime(arr[i] - 1) || isPrime(arr[i] + 1)) {
                primeArr.add(arr[i]);
            }
        }

        System.out.println(primeArr);
        System.out.println();
        System.out.println();

        System.out.println("Sum of Prime array = " + sumArr(primeArr));
        System.out.println();
        System.out.println();

        Level_3(arr);

    }
}
