import java.util.*;
import java.io.*;

class Main {
  public static void main(String[] args) throws IOException {
    
		BufferedReader br = new BufferedReader(new FileReader("milkorder.in"));
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("milkorder.out")));	

    StringTokenizer s = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(s.nextToken());
    int m = Integer.parseInt(s.nextToken());
    int k = Integer.parseInt(s.nextToken());
		int[] social = new int[m];
    int[] req = new int[n + 1];
    int[] taken = new int[n + 1];

    s = new StringTokenizer(br.readLine());
		for(int i = 0; i < m; i++) {
			social[i] = Integer.parseInt(s.nextToken());
		}

    for(int i = 0; i < k ; i++) {
      s = new StringTokenizer(br.readLine());
      int c = Integer.parseInt(s.nextToken());
      int p = Integer.parseInt(s.nextToken());
      req[c] = p;
      taken[p] = c;
    }

    // Try all possible positions for cow 1
    int ans = -1;
    for(int i = 1; i <= n; i++) {
      if( (req[1] == 0 || req[1] == i) && (taken[i] == 0 || taken[i] == 1) ) {
        req[1] = i;
        System.out.println(i);
        if(check(social, req)) {
          ans = i;
          break;
        }
        req[1] = 0;
      }
    }

		pw.println(ans); 

		br.close();
		pw.close();

  }

  // Check whether given social hierarchy and required positions work
	public static boolean check(int[] social, int[] req) {
    int n = req.length - 1;
    int[] ans = new int[n+1];
    for(int i = 1; i <= n; i++) {
      if(req[i] != 0) {
        ans[req[i]] = i;
      }
    }

    int curPos = 1;
    boolean placed = true;
    for(int i = 0; i < social.length; i++) {
      int cow = social[i];
      if(req[cow] != 0) {
        if(req[cow] < curPos) return false;
        else curPos = req[cow] + 1;
        continue;
      }
      placed = false;

      // greedily find next position to place cow 
      while(curPos <= n) {
        if(ans[curPos] == 0) {
          placed = true;
          ans[curPos] = cow;
          break;
        }
        curPos += 1;
      }
    }
    return placed;
	}
}