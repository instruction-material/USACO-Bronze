// adapted from USACO solution: http://www.usaco.org/current/data/sol_prob1_bronze_dec20.html

import java.util.*;
import java.io.*;

class Main {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int[] numbers = new int[7];

    // Input seven space-separated integers
    for (int i = 0; i < 7; i++) {
        numbers[i] = scanner.nextInt();
    }

    // Sort the array in ascending order
    Arrays.sort(numbers);

    // Calculate A, B, and C 
    // A will be the smallest, B will be the second smallest, A + B + C will be the largest number
    int A = numbers[0];
    int B = numbers[1];
    int C = numbers[6] - A - B;

    // Output the result
    System.out.println(A + " " + B + " " + C);

    scanner.close();
    }
  }
