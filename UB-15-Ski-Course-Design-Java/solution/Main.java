/*
ID: your_id_here
LANG: JAVA
TASK: skidesign
*/

import java.io.*;
import java.util.*;

class Main {
  public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new FileReader("skidesign.in"));
		int hills = Integer.parseInt(br.readLine());
		ArrayList<Integer> a = new ArrayList<Integer>();
		for(int i = 0; i < hills; i++) {
			a.add(Integer.parseInt(br.readLine())); 
		}
		Collections.sort(a); //sort hills by size

		int minPrice = Integer.MAX_VALUE;

		//test different intervals between i and i+17
		//i represents elevation
		for(int i = a.get(0); i <= a.get(a.size()-1)-17; i++) {
			
			int price = 0;

			//interval is from min to max (inclusive)
			int min = i;
			int max = i+17;

			//get all hills to be in the interval speficied above
			for(int x = 0; x < a.size(); x++) {
				
				//if the hill is greater than the max of the interval, then add to price the cost of cutting it down to max; if the hill is less than the min of the interval, then add to price the cost of increasing it up to min
				if(a.get(x) > max) {
					price += (a.get(x)-max) * (a.get(x)-max);
				} else if(a.get(x) < min) {
					price += (min-a.get(x)) * (min-a.get(x));
				}

			}

			if(price < minPrice) { //update minPrice
				minPrice = price;
			}

		}

		//output
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("skidesign.out")));	
		pw.println((int)minPrice);
		pw.close();
		br.close();

  }
}