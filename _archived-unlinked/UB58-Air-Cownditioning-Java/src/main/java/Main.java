// adapted from USACO solution: http://www.usaco.org/current/data/sol_prob2_bronze_dec21.htmlc org.junit.jupiter.api.Assertions.assertEquals;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    // store differences between current temps and preferred temps for each stall
    ArrayList<Integer> d = new ArrayList<>();
    {
      int n = Integer.parseInt(in.readLine());
      int[] p = new int[n];
      StringTokenizer st = new StringTokenizer(in.readLine());
      for(int i = 0; i < n; i++) p[i] = Integer.parseInt(st.nextToken());
      int[] t = new int[n];
      st = new StringTokenizer(in.readLine());
      for(int i = 0; i < n; i++) t[i] = Integer.parseInt(st.nextToken());
      for(int i = 0; i < n; i++) d.add(p[i] - t[i]);
    }
    // do as many increments/decrements as possible until some element becomes zero
    int ans = 0;
    while(!d.isEmpty()) {
      if(d.get(d.size()-1) == 0) {
        d.remove(d.size()-1);
        continue;
      }
      boolean positive = d.get(d.size()-1) > 0;
      int amtChange = 1;
      int delta = Math.abs(d.get(d.size()-1));
      // find the maximum possible delta for consecutive stalls with the same sign
      while(amtChange < d.size()) {
        if(d.get(d.size()-1-amtChange) == 0) break;
        if((d.get(d.size()-1-amtChange) > 0) != positive) break;
        delta = Math.min(delta, Math.abs(d.get(d.size()-1-amtChange)));
        amtChange++;
      }
      ans += delta;
      for(int i = 0; i < amtChange; i++) {
        if(d.get(d.size()-1-i) > 0) {
          d.set(d.size()-1-i, d.get(d.size()-1-i) - delta);
        }
        else {
          d.set(d.size()-1-i, d.get(d.size()-1-i) + delta);	
        }
      }
    }
    System.out.println(ans);
  }
}
