
//adapted from USACO
import java.util.*;

public class Main {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int N = scanner.nextInt();
    int K = scanner.nextInt();
    int T = scanner.nextInt();
    int[] A = new int[K + 1];
    for (int i = 0; i < K; i++) {
      A[i] = scanner.nextInt();
    }
    A[K] = N;
    int[] ans = new int[N];
    Arrays.fill(ans, -1);
    for (int i = 0; i < K; i++) {
      for (int j = A[i]; j < A[i + 1]; j++) {
        int T_prime = T - (j - A[i] + 1);
        int ending_position;
        if (T_prime >= 0) {
          int increase_times = 1 + T_prime / (A[i + 1] - A[i]);
          ending_position = (j + increase_times * (A[i + 1] - A[i])) % N;
        } else {
          ending_position = j;
        }
        ans[ending_position] = j;
      }
    }
    for (int i = 0; i < N; i++) {
      System.out.print(ans[i] + " ");
    }
  }
}
