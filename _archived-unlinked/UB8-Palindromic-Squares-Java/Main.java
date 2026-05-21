/*
ID: your_id_here
LANG: JAVA
TASK: palsquare
*/

import java.util.*;
import java.io.*;

class Main {
  public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new FileReader("palsquare.in"));
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("palsquare.out")));

		int base = Integer.parseInt(br.readLine());

		// for all values of x, convert x^2 into this base and check if it's a palindrome
		for(int x = 1; x <= 300; x++) {
			String square = baseConverter((int)Math.pow(x, 2), base);
			if(isPalindrome(square)) {
				pw.println(baseConverter(x, base) + " " + square);
			}
		}

		br.close();
		pw.close();

  }

	// in this method, i is the integer in base 10, and base is the base that i will be converted to
	public static String baseConverter(int i, int base) {
		HashMap <Integer, Character> letters = new HashMap <Integer, Character>();
		letters.put(10, 'A');
		letters.put(11, 'B');
		letters.put(12, 'C');
		letters.put(13, 'D');
		letters.put(14, 'E');
		letters.put(15, 'F');
		letters.put(16, 'G');
		letters.put(17, 'H');
		letters.put(18, 'I');
		letters.put(19, 'J');
		letters.put(20, 'K');

		int quotient = i;
		String answer = "";
		while(quotient != 0) {
			int r = quotient % base;
			if (r >= 10) {
				answer = letters.get(r) + answer;
			} else {
				answer = r + answer;
			}
			quotient = quotient / base;
		}
		return answer;
	}

	public static boolean isPalindrome(String s) {
		// loop through half of the string and check if the character at index i is equal to the character at i away from the end index of the string (i.e. s.length()-1)
		for(int i = 0; i < s.length()/2; i++) {
			if(s.charAt(i) != s.charAt(s.length()-1-i)) {
				return false;
			}
		}
		return true;
	}

}