// adapted from USACO solution: http://www.usaco.org/current/data/sol_prob2_bronze_dec20.html

import java.io.*;
import java.util.*;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    PrintWriter pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));

    // read the number of flowers 
    int n = Integer.parseInt(br.readLine());

    // create array for number of petals for each 
    int[] petals = new int[n];
    StringTokenizer st = new StringTokenizer(br.readLine());
    for(int i = 0; i < n; i++) {
      petals[i] = Integer.parseInt(st.nextToken());
    }

    // count the number of photos that have an average flower
    int photos = 0;

    // loop through all possible combinations of flowers and check if each photo has an average flower
    for(int i = 0; i < n; i++) {
      for(int j = i; j < n; j++) {
        int totalPetals = 0;
        for(int k = i; k <= j; k++) {
          totalPetals += petals[k];
        }
        boolean present = false;
        for(int k = i; k <= j; k++) {
          if(petals[k] * (j-i+1) == totalPetals) {
            present = true;
          }
        }
        if(present) {
          photos++;
        }
      }
    }
    // output the result
    pw.println(photos);
    pw.close();
  }
}