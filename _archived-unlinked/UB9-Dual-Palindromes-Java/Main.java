/*
ID: your_hd_here
LANG: JAVA
TASK: dualpal
*/

import java.util.*;
import java.io.*;

class Main {
  public static void main(String[] args) throws IOException {
    
		BufferedReader br = new BufferedReader(new FileReader("dualpal.in"));
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("dualpal.out")));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int n = Integer.parseInt(st.nextToken());
		int s = Integer.parseInt(st.nextToken());
		
		int count = 0; // counts how many numbers have been found

		int num = s+1; // num has to be greater than s

		while(count < n) {

			int baseCount = 0; // keeps track of in how many bases is num a palindrome

			for(int x = 2; x <= 10; x++) { // go through all bases

				String str = baseConverter(num, x); // convert to base x
				
				if(isPalindrome(str)) {
					baseCount++;
				}

        // once we have reached baseCount = 2, then we have found a number, so write the number to the output file and break out of this loop
				if(baseCount == 2) {
					count++;
					pw.println(num);
					break;
				}
			
			}

			num++;

		}

		pw.close();
		br.close();

  }

	public static String baseConverter(int i, int base) {
		int quotient = i;
		String answer = "";
		while(quotient != 0) {
			int r = quotient % base;
			answer = r + answer;
			quotient = quotient / base;
		}
		return answer;
	}

	public static boolean isPalindrome(String s) {
		for(int i = 0; i < s.length()/2; i++) {
			if(s.charAt(i) != s.charAt(s.length()-1-i)) {
				return false;
			}
		}
		return true;
	}

}