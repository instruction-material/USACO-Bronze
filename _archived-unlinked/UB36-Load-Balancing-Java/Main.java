import java.util.*;
import java.io.*;

class Main {
  public static void main(String[] args) throws IOException {
    
		BufferedReader br = new BufferedReader(new FileReader("balancing.in"));
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("balancing.out")));	
		StringTokenizer s = new StringTokenizer(br.readLine());
		
		//nVal = number of cows
		//bVal = max x and y coordinate (not used)
		int nVal = Integer.parseInt(s.nextToken());
		int bVal = Integer.parseInt(s.nextToken());

		//initialize an array of coordinates, where each coordinate is itself an array with an x and y
		int[][] coordinates = new int[nVal][2];
		
		for(int i = 0; i < nVal; i++) {
			
			//input data
			s = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(s.nextToken());
			int y = Integer.parseInt(s.nextToken());
			//put data into 2D array
			coordinates[i][0] = x;
			coordinates[i][1] = y;
		
		}

		int minCows = Integer.MAX_VALUE; //answer

		//check all values for a that are to the right of a cow, and all values of b that are above a cow
		//this limits the search space so the program can run within time bounds
		for(int i = 0; i < nVal; i++) { //index of x coord
			for(int j = 0; j < nVal; j++) { //index of y coord
				
				//get a value and b value which is directly to the right and above the cow at cowCoordinate
				int a = coordinates[i][0] + 1;
				int b = coordinates[j][1] + 1;

				//cowsInQuadrant holds the number of cows in each quadrant
				int[] cowsInQuadrant = new int[4];
				
				//count how many cows are in each quadrant
				for(int[] coordinate : coordinates) {
					
					//get the x and y coordinates
					int x = coordinate[0];
					int y = coordinate[1];

					//increment cowsInQuadrant at the appropriate index by comparing x and y to a and b respectively
					if(x < a && y < b) {
						cowsInQuadrant[0]++;
					} else if(x < a && y > b) {
						cowsInQuadrant[1]++;
					} else if(x > a && y > b) {
						cowsInQuadrant[2]++;
					} else {	
						cowsInQuadrant[3]++;
					}

				}

				//get the max number of cows between the four numbers in the maxCowsInQuadrant array
				int maxCowsInQuadrant = Math.max(Math.max(Math.max(cowsInQuadrant[0], cowsInQuadrant[1]), cowsInQuadrant[2]), cowsInQuadrant[3]);

				//update minCows
				minCows = Math.min(maxCowsInQuadrant, minCows);

			}
		}

		pw.println(minCows); //output
		
		br.close();
		pw.close();

  }
}