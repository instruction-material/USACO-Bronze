import java.util.*;
import java.io.*;

class Main {
  public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new FileReader("billboard.in"));
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("billboard.out")));

		//lawnmower billboard
		StringTokenizer s = new StringTokenizer(br.readLine());
		int x1 = Integer.parseInt(s.nextToken());
		int y1 = Integer.parseInt(s.nextToken());
		int x2 = Integer.parseInt(s.nextToken());
		int y2 = Integer.parseInt(s.nextToken());
		
		//cow feed billboard
		s = new StringTokenizer(br.readLine());
		int x3 = Integer.parseInt(s.nextToken());
		int y3 = Integer.parseInt(s.nextToken());
		int x4 = Integer.parseInt(s.nextToken());
		int y4 = Integer.parseInt(s.nextToken());

		//four corners of the lawnmower billboard are:
		//(x1, y1)
		//(x1, y2)
		//(x2, y1)
		//(x2, y2)
		//check how many of those corners are covered by the cow feed billboard

		int numCornersCovered = 0;
		if(cornerIsCovered(x1, y1, x3, y3, x4, y4)) {
			numCornersCovered++;
		}
		if(cornerIsCovered(x1, y2, x3, y3, x4, y4)) {
			numCornersCovered++;
		}	
		if(cornerIsCovered(x2, y1, x3, y3, x4, y4)) {
			numCornersCovered++;
		}
		if(cornerIsCovered(x2, y2, x3, y3, x4, y4)) {
			numCornersCovered++;
		}

		int area = 0;
		
		if(numCornersCovered == 4) {
			
			//the whole lawnmower billboard is covered
			area = 0;
		
		} else if(numCornersCovered < 2) {
			
			//you need to cover the whole lawnmower billboard
			area = (x2-x1) * (y2-y1);
		
		} else {

			//find the area of the lawnmower billboard that you need to cover by finding the width and height of the part that is already covered and subtracting that from the area of the billboard
			int width = Math.min(x2, x4) - Math.max(x1, x3);
			int height = Math.min(y2, y4) - Math.max(y1, y3);
			area = (x2-x1) * (y2-y1) - (width * height);

		}
		
		pw.println(area);
		br.close();
		pw.close();

	}

	//returns true if corner at (x, y) is covered by rectangle bounded by (x1, y1) and (x2, y2)
	public static boolean cornerIsCovered(int x, int y, int x1, int y1, int x2, int y2) {
		return (x >= x1 && x <= x2 && y >= y1 && y <= y2);
	}

}