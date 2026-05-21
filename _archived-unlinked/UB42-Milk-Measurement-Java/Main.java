import java.util.*;
import java.io.*;

class Main {
  public static void main(String[] args) throws IOException {
		
		//input
		BufferedReader br = new BufferedReader(new FileReader("measurement.in"));
		int entries = Integer.parseInt(br.readLine());
		
		HashMap<Integer, int[]> entry = new HashMap<Integer, int[]>();

		for(int i = 0; i < entries; i++) { //loop through each of the entries

			StringTokenizer st = new StringTokenizer(br.readLine());

			//DAY

			int day = Integer.parseInt(st.nextToken());
			
			//COW

			//Bessie, Elsie, and Mildred
			//   0      1          2

			String c = st.nextToken();
			int cow = 0;
			
			if(c.equals("Bessie")) {
				cow = 0;
			} else if(c.equals("Elsie")) {
				cow = 1;
			} else {
				cow = 2;
			}

			//MILK

			//s is the string form of the whole number
			//milk is the int number without the sign
			String s = st.nextToken();
			int milk = Integer.parseInt(s.substring(1));
			
			//make milk negative if necessary
			if (s.charAt(0) == '-') {
				milk *= -1;
			}

			//ENTER DATA INTO ENTRY HASHMAP

			int[] cowMilk = {cow, milk};
			entry.put(day, cowMilk);

		}
		br.close();

		//SORT THE HASHMAP BY KEY (DAY)

		ArrayList<Integer> keys = new ArrayList<>(entry.keySet());
		Collections.sort(keys);
		
		/*

		DISPLAY CODE!!
	
		max cow(s) | display
		--------------------	
		0          |  0
		1          |  1
		2          |  2
		0, 1       |  3
		0, 2       |  4
		1, 2       |  5
		0, 1, 2    |  6
	
		*/

		//all cows start with 7 milk gallons so display starts at 6 (all three cows are tied)
		int display = 6; //cow(s) to display, see code above
		int zero = 7; //milk for cow 0
		int one = 7; //milk for cow 1
		int two = 7; //milk for cow 2
		
		int changes = 0; //number of display changes (answer)

		for(int i = 0; i < entries; i++) { //loop through each of the entries
			
			//data
			int day = keys.get(i);
			int cow = entry.get(day)[0];
			int milk = entry.get(day)[1];

			//add the milk to the appropriate cow (0, 1, or 2)
			if (cow == 0) {
				zero += milk;
			} else if (cow == 1) {
				one += milk;
			} else {
				two += milk;
			}
			
			//caculate the new display number (see code above)
			int newDisplay;
			if(zero > one && zero > two) { 
				newDisplay = 0;
			} else if(one > zero && one > two) { 
				newDisplay = 1;
			} else if(two > zero && two > one) { 
				newDisplay = 2;
			} else if(zero == one && zero > two) { 
				newDisplay = 3;
			} else if(zero == two && zero > one) { 
				newDisplay = 4;
			} else if(two == one && one > zero) { 
				newDisplay = 5;
			} else {
				newDisplay = 6;
			}


			//if the new display is different from the current display, then change the display and increment changes
			if(newDisplay != display) {
				display = newDisplay;
				changes++;
			}
	
		}
		
		//output changes
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("measurement.out")));
		pw.println(changes);
		pw.close();

  }
}