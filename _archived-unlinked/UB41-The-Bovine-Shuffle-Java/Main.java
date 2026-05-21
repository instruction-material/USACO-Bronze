import java.util.*;
import java.io.*;

class Main {
  public static void main(String[] args) throws IOException {
		
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("shuffle.out")));
		BufferedReader br = new BufferedReader(new FileReader("shuffle.in"));

		//num is the number of cows
		int num = Integer.parseInt(br.readLine());
		
		//shuffle contains the cow positions describing the shuffle
		int[] shuffle = new int[num];
		StringTokenizer s = new StringTokenizer(br.readLine());
		for(int i = 0; i < num; i++) {
			shuffle[i] = Integer.parseInt(s.nextToken());
		}

		//finalOrder contains the order of the cows based on ID number after the three shuffles
		int[] finalOrder = new int[num];
		s = new StringTokenizer(br.readLine());
		for(int i = 0; i < num; i++) {
			finalOrder[i] = Integer.parseInt(s.nextToken());
		}

		//get the starting order and output it
		int[] startingOrder = getStartingOrder(shuffle, finalOrder);
		for(int i : startingOrder) {
			pw.println(i);
		}

		pw.close();
		br.close();

  }
	
	//perform three "reverse shuffles" to get the original starting order
	public static int[] getStartingOrder(int[] shuffle, int[] finalOrder) {

		int[] shuffle1 = reverseShuffle(shuffle, finalOrder);int[] shuffle2 = reverseShuffle(shuffle, shuffle1);
		int[] shuffle3 = reverseShuffle(shuffle, shuffle2);
		return shuffle3;

	}
	
	//takes in the shuffle and the result of the shuffle and returns the starting order (all of type int[])
	public static int[] reverseShuffle(int[] shuffle, int[] finalOrder) {

		int[] startingOrder = new int[finalOrder.length];
		for(int i = 0; i < finalOrder.length; i++) {
			startingOrder[i] = finalOrder[shuffle[i]-1];
		}
		return startingOrder;

	}

}