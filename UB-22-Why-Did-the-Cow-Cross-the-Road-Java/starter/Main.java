// ADDED: distinct unfinished learner; the original reference remains in solution/.
import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Scanner;

class Main {
    public static void main(String[] args) throws IOException {
        int[][] observations;
        try (Scanner input = new Scanner(new File("crossroad.in"))) {
            if (!input.hasNextInt()) throw new IllegalArgumentException("Expected observation count.");
            int count = input.nextInt();
            if (count < 1 || count > 100) throw new IllegalArgumentException("Count must be in 1..100.");
            observations = new int[count][2];
            for (int i = 0; i < count; i++) {
                if (!input.hasNextInt()) throw new IllegalArgumentException("Expected cow ID.");
                int cow = input.nextInt();
                if (!input.hasNextInt()) throw new IllegalArgumentException("Expected side.");
                int side = input.nextInt();
                if (cow < 1 || cow > 10 || (side != 0 && side != 1))
                    throw new IllegalArgumentException("Cow must be in 1..10 and side in 0..1.");
                observations[i][0] = cow;
                observations[i][1] = side;
            }
            if (input.hasNext()) throw new IllegalArgumentException("Unexpected trailing input.");
        }
        try {
            int crossings = countCrossings(observations);
            try (PrintWriter output = new PrintWriter("crossroad.out")) {
                output.println(crossings);
            }
        } catch (UnsupportedOperationException unfinished) {
            System.err.println(unfinished.getMessage());
            System.exit(2);
        }
    }

    // ADDED: complete only this algorithm; preserve the supplied file-I/O driver.
    static int countCrossings(int[][] observations) {
        throw new UnsupportedOperationException("TASK: crossing transitions"); // ADDED
    }
}
