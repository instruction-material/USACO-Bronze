import java.util.*;
import java.io.*;

class Main {
  public static void main(String[] args) throws IOException{

		BufferedReader br = new BufferedReader(new FileReader("reduce.in"));
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("reduce.out")));	

		//input
		int n = Integer.parseInt(br.readLine());
		int[][] cowCoordinates = new int[n][2];
		for(int i = 0; i < n; i++) {
			StringTokenizer s = new StringTokenizer(br.readLine());
			cowCoordinates[i][0] = Integer.parseInt(s.nextToken());
			cowCoordinates[i][1] = Integer.parseInt(s.nextToken());
		}
		
		/* 
		we only need to keep track of 8 numbers:
    • smallest (x1) and second smallest (x2) x-coordinate
    • largest (x3) and second largest (x4) x-coordinate
   	• smallest (y1) and second smallest (y2) y-coordinate
    • largest (y3) and second largest (y4) y-coordinate
		*/

    int x1 = 40000;
    int x2 = 40000;
    int x3 = 0;
    int x4 = 0;
    int y1 = 40000;
    int y2 = 40000;
    int y3 = 0;
    int y4 = 0;

		int minArea = Integer.MAX_VALUE;

		for(int[] cowCoord : cowCoordinates) {
			
			int x = cowCoord[0];
			int y = cowCoord[1];

			if(x < x1) {
            x2 = x1;
            x1 = x;
			} else if(x < x2) {
            x2 = x;
			}
            
    	if(x > x3) {
            x4 = x3;
            x3 = x;
			} else if(x > x4) {
            x4 = x;
			}
        
    	if(y < y1) {
            y2 = y1;
            y1 = y;
			} else if (y < y2) {
            y2 = y;
			}
            
			if(y > y3) {
					y4 = y3;
					y3 = y;
			} else if(y > y4) {
					y4 = y;
			}

		}

		minArea = (x3-x1)*(y3-y1);

		/*
		now, check each point and see if it is on the current fence border
    -> if it is, then pretend to remove it and update to the second smallest/largest accordingly
		*/

		for(int[] cowCoord : cowCoordinates) {
			
			int x = cowCoord[0];
			int y = cowCoord[1];

        int minX = x1;
        int maxX = x3;
        int minY = y1;
        int maxY = y3;

        if(x == x1) {
            minX = x2;
				}
        if(x == x3) {
            maxX = x4;
				}
        if(y == y1) {
            minY = y2;
				}
        if(y == y3) {
            maxY = y4;
				}

        minArea = Math.min(minArea, (maxX-minX)*(maxY-minY));

		}

		//output
		pw.println(minArea);
		br.close();
		pw.close();

  }
}