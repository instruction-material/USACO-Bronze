import java.util.*;
import java.io.*;

class Main {
  public static void main(String[] args) throws IOException {
    
		BufferedReader br = new BufferedReader(new FileReader("circlecross.in"));
		String s = br.readLine();
		br.close();
		
		int pairs = 0;

		for(int i = 0; i < s.length(); i++) {
			
			//index i is the entry and exit1 is the exit for the character at index i
			int exit1 = s.indexOf(s.charAt(i), s.indexOf(s.charAt(i)) + 1);

			//exit1 = -1 -> your other character has already passed
			//exit1 = 0 -> your other character is right next to this one
			if(exit1 != -1 && exit1 != 0) {
				
				//loop through the characters from entry to exit
				for(int j = i; j < exit1+1; j++) {
					
					//entry and exit for character at index j
					int entry2 = j;
					int exit2 = s.indexOf(s.charAt(entry2), s.indexOf(s.charAt(entry2)) + 1);

					//if you haven't passed this character yet
					if(exit2 != -1) {
						//if exit1 is in between entry2 and exit2, then you found a crossing pair
						if(entry2 < exit1 && exit1 < exit2) {
							pairs++;
						}
					}

				}

			}

		}

		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("circlecross.out")));
		pw.println(pairs);
		pw.close();

  }
}