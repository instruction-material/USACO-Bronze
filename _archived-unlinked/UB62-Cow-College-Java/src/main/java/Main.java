
//adapted from USACO
import java.util.Arrays;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();
    int[] a = new int[n];
    for (int i = 0; i < n; i++) {
      a[i] = in.nextInt();
    }
    long best = -1L;
    int tuit = 0;
    Arrays.sort(a);
    for (int i = n - 1; i >= 0; i--) {
      long cur = (long) (n - i) * (long) a[i];
      if (cur >= best) {
        best = cur;
        tuit = a[i];
      }
    }
    System.out.println(best + " " + tuit);
  }
}