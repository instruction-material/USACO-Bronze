// adapted from USACO solution: http://www.usaco.org/current/data/sol_prob1_bronze_open22.html

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(in.readLine());
        char[] order = in.readLine().toCharArray();
        int max_reversals = 0;
       // Iterate through even positions from right to left
        for (int j = n - 2; j >= 0; j -= 2) {
            // check that there is a switch between cow breeds, the current position is G, and parity is even
            if (order[j] != order[j + 1] && (order[j] == 'G') == (max_reversals % 2 == 0)) {
              max_reversals++;
            }
        }
        System.out.println(max_reversals);
    }
}