import java.util.*;
import java.io.*;

class Main {
  public static void main(String[] args) throws IOException {
    
		BufferedReader br = new BufferedReader(new FileReader("pails.in"));
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("pails.out")));	
		StringTokenizer s = new StringTokenizer(br.readLine());

		//input
		
		int x = Integer.parseInt(s.nextToken());
		int y = Integer.parseInt(s.nextToken());
		int m = Integer.parseInt(s.nextToken());

		//try every combination of the small and medium pails
    //at most, the total number of pails has to be less than m/x
		
		int maxMilk = 0;
		int maxPails = m/x;
		
		for(int xPails = 0; xPails <= maxPails; xPails++) {
			for(int yPails = 0; yPails <= maxPails-xPails; yPails++) {

				int totalMilk = x*xPails + y*yPails;
				if(totalMilk > maxMilk && totalMilk <= m) {
					maxMilk = totalMilk;
				}
				
			}	
		}

		//output
	
		pw.println(maxMilk);
		br.close();
		pw.close();

  }
}