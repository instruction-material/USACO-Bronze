import java.io.*;
import java.util.*;

class Main {
  public static void main(String[] args) throws IOException {
    
		//ID number - 1 corresponds to the side of the road the cow is currently on
		int[] cows = {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1};
		//sum is the number of crossings
		int sum = 0;

		BufferedReader br = new BufferedReader(new FileReader("crossroad.in"));
		int observations = Integer.parseInt(br.readLine());

		for(int i = 0; i < observations; i++) {
		
			StringTokenizer st = new StringTokenizer(br.readLine());
			int cow = Integer.parseInt(st.nextToken());
			int side = Integer.parseInt(st.nextToken());

			//if the observed cow is not being observed for the first time (if their side number is -1, that means they haven't been observed yet) AND if the observed cow is on a different side than what was last observed
			if(cows[cow-1] != side && cows[cow-1] != -1) {
				sum++; //cow has crossed
			}
			cows[cow-1] = side; //update what side the cow is on

		}

		br.close();
		
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("crossroad.out")));
		pw.println(sum);
		pw.close();

  }
}