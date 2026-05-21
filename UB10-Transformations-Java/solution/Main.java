/*
ID: your_id_here
LANG: JAVA
TASK: transform
*/

import java.util.*;
import java.io.*;

class Main {
  public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new FileReader("transform.in"));

		int length = Integer.parseInt(br.readLine());
		
		// a1 is before transformation
		// a2 is after transfomation
		char[][] a1 = new char[length][length];
		char[][] a2 = new char[length][length];

		for(int i = 0; i < length; i++) {
			String s = br.readLine();
			for(int j = 0; j < length; j++) {
				a1[i][j] = s.charAt(j);
			}
		}

		for(int i = 0; i < length; i++) {
			String s = br.readLine();
			for(int j = 0; j < length; j++) {
				a2[i][j] = s.charAt(j);
			}
		}

		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("transform.out")));

		if (check(a2, one(a1))) {
			pw.println("1");
		}
		else if(check(a2, two(a1))) {
			pw.println("2");
		}
		else if(check(a2, three(a1))) {
			pw.println("3");
		}
		else if(check(a2, four(a1))) {
			pw.println("4");
		}
		else if(check(a2, fiveOne(a1)) || check(a2, fiveTwo(a1)) || check(a2, fiveThree(a1))) {
			pw.println("5");
		}
		else if(check(a1, a2)) {
			pw.println("6");
		}
		else {
			pw.println("7");
		}

		br.close();
		pw.close();

  }
	
	// check() returns true if the arrays a2 and a3 contain the exact same contents, and false otherwise
	public static boolean check(char[][] a2, char[][] a3) {
		for(int i=0; i<a2.length; i++) {	
			for(int j=0; j<a2[i].length; j++) {
				if(a2[i][j] != a3[i][j]) {
					return false;
				}
			}
		}
		return true;
	}

	// one() rotates a1 90 degrees clockwise
	public static char[][] one(char[][] a1) {
		char[][] transform = new char[a1.length][a1[0].length];
		for(int i=0; i<a1.length; i++) {	
			for(int j=0; j<a1[i].length; j++) {
				transform[j][a1.length-1-i] = a1[i][j];
			}
		}
		return transform;
	}

	// two() rotates a1 180 degrees clockwise
	public static char[][] two(char[][] a1) {
		return one(one(a1));
	}

	// three() rotates a1 270 degrees clockwise
	public static char[][] three(char[][] a1) {
		return one(one(one(a1)));
	}

	// four() reflects a1 horizontally 
	public static char[][] four(char[][] a1) {
		char[][] transform = new char[a1.length][a1[0].length];
		for(int i=0; i<a1.length; i++) {	
			for(int j=0; j<a1[i].length; j++) {
				transform[i][a1.length-1-j] = a1[i][j];
			}
		}
		return transform;
	}

	// fiveOne() returns a1 reflected horizontally and then rotated 90 degrees clockwise
	public static char[][] fiveOne(char[][] a1) {
		return one(four(a1));
	}

	// fiveTwo() returns a1 reflected horizontally and then rotated 180 degrees clockwise
	public static char[][] fiveTwo(char[][] a1) {
		return two(four(a1));
	}

	// fiveThree() returns a1 reflected horizontally and then rotated 270 degrees clockwise
	public static char[][] fiveThree(char[][] a1) {
		return three(four(a1));
	}

}