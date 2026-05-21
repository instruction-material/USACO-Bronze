import java.util.*;
import java.io.*;

class Main {
  public static void main(String[] args) throws IOException {
    
		BufferedReader br = new BufferedReader(new FileReader("diamond.in"));
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("diamond.out")));	
		StringTokenizer s = new StringTokenizer(br.readLine());

		int n = Integer.parseInt(s.nextToken()); //number of diamonds
		int k = Integer.parseInt(s.nextToken()); //greatest difference in size
		int[] diamonds = new int[n]; //stores sizes of the diamonds
		for(int i = 0; i < n; i++) {
			diamonds[i] = Integer.parseInt(br.readLine());
		}

		int max = 0; //max number of diamonds that can be displayed (aka - the output)

		//loop through each of the diamonds and see how many diamonds can be displayed with it
		for(int diamondToBeDisplayed : diamonds) {

			int display = 0; //how many diamonds can be displayed

			//see if each diamond can be displayed with diamondToBeDisplayed
			for(int diamond : diamonds) {

				//a diamond can only be displayed if the difference between the two is smaller than k
				//also, the diamond has to be greater than or equal to diamondToBeDisplayed so the difference isn't negative
				if(diamond >= diamondToBeDisplayed && 
				diamond - diamondToBeDisplayed <= k) {
					display++;
				}

			}

			//update max
			max = Math.max(display, max);

		}

		pw.println(max);
		br.close();
		pw.close();

  }
}