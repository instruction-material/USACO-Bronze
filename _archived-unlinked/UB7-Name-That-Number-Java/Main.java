/*
ID: your_id_here
LANG: JAVA
TASK: namenum
*/

import java.util.*;
import java.io.*;

class Main {

  public static void main(String[] args) throws IOException {

		BufferedReader b = new BufferedReader(new FileReader("namenum.in"));
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("namenum.out")));
		BufferedReader br = new BufferedReader(new FileReader("dict.txt"));

		// read input
		String number = b.readLine();
		b.close();		
		
		boolean isThere = false; //represents if number yields a valid name or not

		// convert each valid name in dict.txt into a number 
		while(true) {
			
			String name = br.readLine();
			String num = "";
			
			// check if there are more names remaining in dict.txt
			if(name != null) {

				// for each character in the name, get its number  and add it to num
				for(int i = 0; i < name.length(); i++) {
					num += letterToNum(name.charAt(i));
				}

				if (num.equals(number)) {
					pw.println(name);
					isThere = true;
				}
		
			} else {
				break;
			}
		
		}

		// output NONE if we have not found a valid name
		if (!isThere) {
			pw.println("NONE");
		}

		pw.close();
		br.close();

	}

	// converts a character to its appropriate number according to the specifications listed in the problem
	public static int letterToNum(char c) {

		int num = (int)c; // get ASCII value of character
		
		if(num > 81) { // for letters after 'q' subtract 1 because 'q' isn't counted
			num -= 1;
		} 
		num -= 65;
		
		// example:
    // a, b, c = 0, 1, 2
		// dividing by 3 makes a, b, c = 0
		// adding 2 makes a, b, c = 2
		// that's why you divide by 3 and add 2

		num /= 3;
		num += 2;
		return num;

	}

}