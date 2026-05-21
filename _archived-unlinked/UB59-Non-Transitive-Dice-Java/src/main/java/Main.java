// adapted from USACO solution: https://usaco.org/current/data/sol_prob2_bronze_jan22.html

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main{

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder out = new StringBuilder();
        for (int n = Integer.parseInt(in.readLine()); n > 0; n--) {
            StringTokenizer tokenizer = new StringTokenizer(in.readLine());
            int[] diceA = new int[4];
            for (int j = 0; j < 4; j++) {
                diceA[j] = Integer.parseInt(tokenizer.nextToken());
            }
            int[] diceB = new int[4];
            for (int j = 0; j < 4; j++) {
                diceB[j] = Integer.parseInt(tokenizer.nextToken());
            }
            String answer = "no";
            for (int w = 1; w <= 10; w++) {
                for (int x = 1; x <= 10; x++) {
                    for (int y = 1; y <= 10; y++) {
                        for (int z = 1; z <= 10; z++) {
                            int[] diceC = {w, x, y, z};
                            if (beats(diceA, diceB) && beats(diceB, diceC) && beats(diceC, diceA)) {
                                answer = "yes";
                            }
                            if (beats(diceB, diceA) && beats(diceA, diceC) && beats(diceC, diceB)) {
                                answer = "yes";
                            }
                        }
                    }
                }
            }
            out.append(answer).append('\n');
        }
        System.out.print(out);
    }

    static boolean beats(int[] dice1, int[] dice2) {
        int diff = 0;
        for (int x : dice1) {
            for (int y : dice2) {
                diff += Integer.signum(x - y);
            }
        }
        return diff > 0;
    }
}
