import java.io.*;
import java.util.*;

class Main {
  public static void main(String[] args) throws IOException { 

		// read input
		BufferedReader br = new BufferedReader(new FileReader("beads.in"));
		br.readLine();
		String input = br.readLine();
		br.close();

		int maxChain = 0;

		// check each possible breaking point
		for(int j = 0; j < input.length(); j++) {
			
			int count1 = 0;
			int count2 = 0;
			int currentPos = j;
			boolean foundChain = false;
			char color = input.charAt(currentPos);
			
			while(true) {
				
				// continue incrementing as long as beads are white
				if(input.charAt(currentPos) == color) {
					count2++;
				// continue incrementing as long as beads are the same color
				} else if(input.charAt(currentPos) == 'w') {
					count2++;
				} else {
					// if the color is white, then update color to be the color you are at now
					if(color == 'w') {
						count2++;
						color = input.charAt(currentPos);
					// if you have reached the end of your chain
					} else {
						// update maxChain appropriately
						if(count1 + count2 > maxChain) {
							if(count1 + count2 > input.length()) {
								maxChain = input.length();
							} else {
								maxChain = count1 + count2;
							}
						}
						count1 = count2;
						count2 = 1;
						color = input.charAt(currentPos);
						if(foundChain) {
							break;
						}
						foundChain = true;
					}
				}
				
				// increment currentPos and loop back around (for circular necklace)
				currentPos++;
				if(currentPos == input.length()) {
					currentPos = 0;
				}
				// if your chain is the whole necklace, then that automatically is the max chain
				if(count2 == input.length()) {
					maxChain = count2;
					break;
				}
			
			}	

		}

		// write output
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("beads.out")));
		pw.println(maxChain);
		pw.close();

	}
}