/*
ID: your_id_here
LANG: JAVA
TASK: barn1
*/

import java.util.*;
import java.io.*;

class Main {
  public static void main(String[] args) throws IOException {
		
    BufferedReader br = new BufferedReader(new FileReader("barn1.in"));
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("barn1.out")));		
		
    StringTokenizer z = new StringTokenizer(br.readLine());
		int m = Integer.parseInt(z.nextToken());
		int s = Integer.parseInt(z.nextToken());
		int c = Integer.parseInt(z.nextToken());

		//stores stall positions of cows
		ArrayList<Integer> stalls = new ArrayList<Integer>();
		
		//input: stalls
		for(int i = 0; i < c; i++) {
			stalls.add(Integer.parseInt(br.readLine()));
		}
		Collections.sort(stalls);

		s = stalls.get(stalls.size()-1) - stalls.get(0);

    ArrayList<Integer> gaps = new ArrayList<Integer>();

    for(int i = 1; i < c; i++) {
      int gap = stalls.get(i) - stalls.get(i-1) - 1; //gap between previous and this cow-occupied stall
      gaps.add(gap);
    }
    
    Collections.sort(gaps, Collections.reverseOrder());

    int sum = 0; //the sum of the large gaps (the stuff you aren't covering)
    for(int i = 0; i < m - 1; i++) {
      if(i >= gaps.size()) 
        break;
      sum += gaps.get(i);
    }

    //output
    pw.println(s-sum+1); 

		br.close();
		pw.close();

  }
}