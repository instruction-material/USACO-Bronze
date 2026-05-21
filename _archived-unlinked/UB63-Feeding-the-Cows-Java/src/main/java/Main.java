
//addapted from USACO
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    for (int t = Integer.parseInt(in.readLine()); t > 0; t--) {
      StringTokenizer tokenizer = new StringTokenizer(in.readLine());
      int n = Integer.parseInt(tokenizer.nextToken());
      int k = Integer.parseInt(tokenizer.nextToken());
      char[] cows = in.readLine().toCharArray();
      int lastGuernseyPatch = -k - 1;
      int lastHolsteinPatch = -k - 1;
      char[] answer = new char[n];
      for (int j = 0; j < n; j++) {
        answer[j] = '.';
      }
      int amtPatches = 0;
      for (int j = k; j < n; j++) {
        if (cows[j - k] == 'G') {
          if ((j - k) - lastGuernseyPatch > k) {
            amtPatches++;
            answer[j] = 'G';
            lastGuernseyPatch = j;
          }
        } else {
          if ((j - k) - lastHolsteinPatch > k) {
            amtPatches++;
            answer[j] = 'H';
            lastHolsteinPatch = j;
          }
        }
      }
      boolean gNeeds = false;
      for (int j = n - 1; j >= 0; j--) {
        if (cows[j] == 'G' && j - lastGuernseyPatch > k) {
          gNeeds = true;
        }
      }
      if (gNeeds) {
        for (int j = n - 1; j >= 0; j--) {
          if (answer[j] == '.') {
            amtPatches++;
            answer[j] = 'G';
            break;
          }
        }
      }
      boolean hNeeds = false;
      for (int j = n - 1; j >= 0; j--) {
        if (cows[j] == 'H' && j - lastHolsteinPatch > k) {
          hNeeds = true;
        }
      }
      if (hNeeds) {
        for (int j = n - 1; j >= 0; j--) {
          if (answer[j] == '.') {
            amtPatches++;
            answer[j] = 'H';
            break;
          }
        }
      }
      System.out.println(amtPatches);
      System.out.println(answer);
    }
  }
}