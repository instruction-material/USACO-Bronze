import java.util.*;
import java.io.*;

class Main {
  public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new FileReader("outofplace.in"));
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("outofplace.out")));

		//number of cows
		int num = Integer.parseInt(br.readLine());
		
		int[] cows = new int[num]; //original lineup
		int[] sortedCows = new int[num]; //sorted lineup

		//intialize cows and sortedCows
		for(int i = 0; i < num; i++) {
			int height = Integer.parseInt(br.readLine());
			cows[i] = height;
			sortedCows[i] = height;
		}
		Arrays.sort(sortedCows); //sort array

		//the trick is that the number of swaps is the number of cows that are in different spots (original lineup versus sorted lineup) minus 1

		int swaps = 0; //number of cows in different spots
		for(int i = 0; i < num; i++) {
			if(sortedCows[i] != cows[i]) { 
				//different cows in spot
				swaps++;
			}
		}

		pw.println(swaps-1); //don't forget to subtract 1!
		br.close();
		pw.close();

  }

}