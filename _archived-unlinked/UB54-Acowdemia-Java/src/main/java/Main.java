//adapted from USACO
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Main {

    static int hIndex(Integer[] papers) {
        int h = papers.length;
        while (h > 0 && papers[h - 1] < h) {
            h--;
        }
        return h;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer = new StringTokenizer(in.readLine());
        int n = Integer.parseInt(tokenizer.nextToken());
        int l = Integer.parseInt(tokenizer.nextToken());
        Integer[] papers = new Integer[n];
        tokenizer = new StringTokenizer(in.readLine());
        for (int j = 0; j < n; j++) {
            papers[j] = Integer.parseInt(tokenizer.nextToken());
        }
        Arrays.sort(papers, Comparator.reverseOrder());
        int h = hIndex(papers);
        if (h != n) {
            for (int j = h; j >= 0 && j > h - l; j--) {
                papers[j]++;
            }
        }
        Arrays.sort(papers, Comparator.reverseOrder());
        System.out.println(hIndex(papers));
    }
}