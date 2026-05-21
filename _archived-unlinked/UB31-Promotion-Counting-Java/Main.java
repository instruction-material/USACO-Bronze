import java.io.*;
import java.util.*;

class Main {
  public static void main(String[] args) throws IOException {
		
		//input
		BufferedReader br = new BufferedReader(new FileReader("promote.in"));
		int[][] a = new int[4][2];
		for(int i = 0; i < 4; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			a[i][0] = Integer.parseInt(st.nextToken());
			a[i][1] = Integer.parseInt(st.nextToken());
		}
		br.close();

		int gp = 0; //gold to platinum
		int sg = 0; //silver to gold
		int bs = 0; //bronze to silver

		//promoted from gold to platinum = num platinum after - num platinum before
		gp = a[3][1] - a[3][0];

		//promoted from silver to gold = num in gold or platinum after - num in gold or platinum before 
		sg = (a[3][1] + a[2][1]) - (a[3][0] + a[2][0]);

		//promoted from bronze to silver = num in silver or gold or platinum after - num in silver or gold or platinum before
		bs = (a[3][1] + a[2][1] + a[1][1]) - (a[3][0] + a[2][0]+ a[1][0]);
		
		//output
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("promote.out")));	
		pw.println(bs);
		pw.println(sg);
		pw.println(gp);
		pw.close();

  }
}