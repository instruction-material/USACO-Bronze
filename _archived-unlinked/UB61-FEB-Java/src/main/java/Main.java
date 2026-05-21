
// Adapted from USACO
import java.util.*;

public class Main {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int N = scanner.nextInt();
    scanner.nextLine(); // consume newline
    char[] S = scanner.nextLine().toCharArray();
    if (new String(S).chars().filter(c -> c == 'F').count() == N) {
      S[0] = 'E';
    }
    List<Integer> positions = new ArrayList<>();
    for (int i = 0; i < N; i++) {
      if (S[i] != 'F') {
        positions.add(i);
      }
    }
    int ones = positions.get(0) + N - 1 - positions.get(positions.size() - 1);
    int mn = 0, mx = 0;
    for (int i = 0; i < positions.size() - 1; i++) {
      int a = positions.get(i), b = positions.get(i + 1);
      mn += ((b - a) & 1) ^ (S[a] != S[b] ? 1 : 0);
      mx += b - a - (S[a] != S[b] ? 1 : 0);
    }
    List<Integer> ans = new ArrayList<>();
    for (int i = mn; i <= ones + mx; i += 1 + (ones == 0 ? 1 : 0)) {
      ans.add(i);
    }
    System.out.println(ans.size());
    for (int level : ans) {
      System.out.println(level);
    }
  }
}
