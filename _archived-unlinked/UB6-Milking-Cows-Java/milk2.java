/*
ID: your_id_here
LANG: JAVA
TASK: milk2
*/

import java.util.*;
import java.io.*;

public class milk2 {
  public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new FileReader("milk2.in"));

		// number of farmers (first line of input)
    int farmers = Integer.parseInt(br.readLine());

		// milk is a timeline, where true indicates that a cow is being milked, and false indicates that no cows are being milked
		boolean[] milk = new boolean[1000001];

		// find maximum end time and minimum start time
		int min = 1000000;
		int max = 0;

		for(int i = 0; i < farmers; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int start = Integer.parseInt(st.nextToken());
			int end = Integer.parseInt(st.nextToken());

			if (start < min) {
				min = start;
			}

			if (end > max) {
				max = end;
			}
			
      // update timeline
			for(int x = start; x < end; x++) {
				milk[x] = true;
			}
  	}

		br.close();

		int maxTrue = 0; // maximum milking time
		int maxFalse = 0; // maximum non-milking time
		int trueCount = 0; // milking time
		int falseCount = 0; // non-milking time

		// represents whether the previous timepoint had a cow being milked (true) or no cow being milked (false)
		boolean prev = milk[min];

		// go through array and find the max true and max false values
		for(int i = min; i <= max; i++) {
			
			if (milk[i]) { // if the cow is being milked
			
				if (!prev) { // if previous cow wasn't being milked

					// you are switching from a non-milk interval to a milk interval, so you have to check if you have a new maxFalse (max non-milk interval)

					if(falseCount > maxFalse) {
						maxFalse = falseCount;
					}
					falseCount = 0;
					prev = true;
				
				}
				// since a cow is being milked, incresase trueCount
				trueCount++;
			
			} else { // if no cow is being milked

				if (prev) { // if the previous cow was being milked

					// you are switching from a milk interval to a non-milk interval so you have to check if you have a new maxTrue (max milk interval)

					if(trueCount > maxTrue) { 
						maxTrue = trueCount;
					}
					trueCount = 0;
					prev = false; 
				
				}
				// since a cow isn't being milked, incresase falseCount
				falseCount++;
			
			}

		}

		// write output
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("milk2.out")));
		pw.print(maxTrue + " " + maxFalse);
		pw.println();
		pw.close();
	}
}