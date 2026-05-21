import java.util.*;
import java.io.*;

class Main {
  public static void main(String[] args) throws IOException {
    
		BufferedReader br = new BufferedReader(new FileReader("cowtip.in"));
		int sq = Integer.parseInt(br.readLine());
		int[][] square = new int[sq][sq];

		//intialize square 2D array
		for(int i = 0; i < sq; i++) {
			String s = br.readLine(); //row string
			for(int j = 0; j < sq; j++) {
				//get numeric form of the character in row s 
				int value = Character.getNumericValue(s.charAt(j));
				square[i][j] = value;
			}	
		}
		br.close();

		//start from the bottom right corner and flip cows only if the bottom right of the upper-left rectangle is a 1; numFlips keeps track of the total # of flips
		int numFlips = 0;
		for(int i = sq-1; i >= 0; i--) {
			for(int j = sq-1; j >= 0; j--) {
				if(square[i][j] == 1) {
					numFlips++;
					flipOver(i, j, square);
				}
			}
		}

		//output numFlips
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("cowtip.out")));
		pw.println(numFlips);
		pw.close();
		
  }

	//flips over all cows in range [0-i][0-j] in 2D array a
	public static void flipOver(int i, int j, int[][] a) {

		for(int x = i; x >= 0; x--) {
			for(int y = j; y >= 0; y--) {
				//switch 1 to 0 or 0 to 1
				if(a[x][y] == 1) {
					a[x][y] = 0;
				} else { 
					a[x][y] = 1;
				}
			}	
		}

	}

}