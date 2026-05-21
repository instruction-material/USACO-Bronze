/*
ID: your_id_here
LANG: JAVA
TASK: ride
*/

import java.io.*;
import java.util.*;

class Main {
  public static void main(String[] args) throws IOException {
    
		// read input
		BufferedReader br = new BufferedReader(new FileReader("ride.in"));
		String input1 = br.readLine();
		String input2 = br.readLine();
		br.close();

		// the final numbers that we will compare
		int number1 = 1;
		int number2 = 1;

		// for input1, get the product of the numerical versions of the letters, and then take the product % 47
		// to convert a char to a number, cast it to an int to get its ASCII value and subtract 64
		// e.g. the ASCII value for 'A' is 65, and 65 - 64 = 1

		for(int i = 0; i < input1.length(); i++) {
			number1 *= ((int)(input1.charAt(i)) - 64);
		}
		number1 = number1 % 47;
		
		// same thing for input2

		for(int i = 0; i < input2.length(); i++) {
			number2 *= ((int)(input2.charAt(i)) - 64);
		}
		number2 = number2 % 47;

		// if the numbers are equal then the group can go, otherwise the group has to stay

		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("ride.out")));

		if (number1 == number2) {
			pw.println("GO"); 
		} else { 
			pw.println("STAY"); 
		}

		pw.close();

  }
}