// adapted from USACO solution: http://www.usaco.org/current/data/sol_prob2_bronze_feb22.html

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(in.readLine());
        StringTokenizer tokenizerA = new StringTokenizer(in.readLine());
        StringTokenizer tokenizerB = new StringTokenizer(in.readLine());
        int[] a = new int[n];
        int[] b = new int[n];
        for (int j = 0; j < n; j++) {
            a[j] = Integer.parseInt(tokenizerA.nextToken());
            b[j] = Integer.parseInt(tokenizerB.nextToken());
        }
        int answer = 0;
        boolean[] moved = new boolean[n + 1];
        int k = 0;
        for (int j = 0; j < n; j++) {
            while (moved[a[k]]) {
                k++;
            }
            if (b[j] == a[k]) {
                k++;
            } else {
                answer++;
                moved[b[j]] = true;
            }
        }
        System.out.println(answer);
    }
}