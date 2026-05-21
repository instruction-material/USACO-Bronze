import java.util.*;
import java.io.*;

class Main {
  public static void main(String[] args) throws IOException {
    
		BufferedReader br = new BufferedReader(new FileReader("billboard.in"));

		//a 2D array mimics Bessie's view
		int[][] bill = new int[2001][2001];

		int area1 = 0; //area of billboard 1
		int area2 = 0; //area of billboard 2

		int overlap = 0; //how much overlap there is between the billboards and the truck

		for(int i = 0; i < 3; i++) { //get 3 lines of input
			
			//get lower-left and upper-right coordinates
			StringTokenizer st = new StringTokenizer(br.readLine());
			int x1 = Integer.parseInt(st.nextToken());
			int y1 = Integer.parseInt(st.nextToken());
			int x2 = Integer.parseInt(st.nextToken());
			int y2 = Integer.parseInt(st.nextToken());

			if(i == 0) { //billboard 1
				area1 = (x2-x1)*(y2-y1);
			} else if (i == 1) { //billboard 2
				area2 = (x2-x1)*(y2-y1);
			}

			//fill in the rectangle section of the 2D array
			for(int x = x1; x < x2; x++) {
				for(int y = y1; y < y2; y++) {
					
					//arrayX and arrayY are the indexes in the 2D array (because points span from -1000 to +1000)
					int arrayX = x+1000;
					int arrayY = y+1000;
					
					//0 = nothing there
					//1 = either billboard or truck there
					//2 = billboard and truck are there (since billboards do not overlap)

					//if there is nothing there (0), then put something there (1)
					if(bill[arrayX][arrayY] == 0) {
						bill[arrayX][arrayY] = 1;
					
					//if there is something there already (1), then make it an overlap (2)
					} else if (bill[arrayX][arrayY] == 1) {
						bill[arrayX][arrayY] = 2;
						overlap++; //increment overlap variable
					}

				}
			}

		}

		//the visible area of the billboards is the area of billboard 1 + the area of billboard 2 - the area of overlap with the truck
		int answer = area1 + area2 - overlap;
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("billboard.out")));
		pw.println(answer);
		pw.close();
		br.close();

  }
}