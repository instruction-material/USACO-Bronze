import java.io.*;
import java.util.*;

class Main {
  public static void main(String[] args) throws IOException {

		//keeps track of all of the points visited
		ArrayList<Point> points = new ArrayList<Point>();
		
		//smallest time difference
		int x = Integer.MAX_VALUE;

		//get the number of steps
		BufferedReader br = new BufferedReader(new FileReader("mowing.in"));
		int n = Integer.parseInt(br.readLine());
		
		Point current = new Point(0, 0);
		points.add(current);

		for(int i = 0; i < n; i++) { //loop through steps

			//input
			StringTokenizer st = new StringTokenizer(br.readLine());
			String ch = st.nextToken(); //N, S, W, or E
			int num = Integer.parseInt(st.nextToken()); //steps

			if(ch.equals("N")) { //north
				//for each step, increment y and create a new Point and add it to the list
				for(int j = 0; j < num; j++) {
					current.y++;
					Point t = new Point(current.x, current.y);
					int index = contains(points, current);
					if(index != -1) { //if t is in the list
						//get the time difference and set x is time difference is smaller than it
						int timeDifference = points.size()-index-1;
						if(timeDifference < x) {
							x = timeDifference;
						}
					}
					points.add(points.size()-1, t);
				}
			} else if(ch.equals("S")) { //south
				//for each step, decrement y and create a new Point and add it to the list
				for(int j = 0; j < num; j++) {
					current.y--;				
					Point t = new Point(current.x, current.y);
					int index = contains(points, current);
					if(index != -1) { //if t is in the list
						//get the time difference and set x is time difference is smaller than it
						int timeDifference = points.size()-index-1;
						if(timeDifference < x) {
							x = timeDifference;
						}
					}
					points.add(points.size()-1, t);
				}
			} else if(ch.equals("W")) { //west
				//for each step, decrement x and create a new Point and add it to the list
				for(int j = 0; j < num; j++) {
					current.x--;
					Point t = new Point(current.x, current.y);
					int index = contains(points, current);
					if(index != -1) { //if t is in the list
						//get the time difference and set x is time difference is smaller than it
						int timeDifference = points.size()-index-1;
						if(timeDifference < x) {
							x = timeDifference;
						}
					}
					points.add(points.size()-1, t);
				}
			} else { //east
				//for each step, increment x and create a new Point and add it to the list
				for(int j = 0; j < num; j++) {
					current.x++;
					Point t = new Point(current.x, current.y);
					int index = contains(points, current);
					if(index != -1) { //if t is in the list
						//get the time difference and set x is time difference is smaller than it
						int timeDifference = points.size()-index-1;
						if(timeDifference < x) {
							x = timeDifference;
						}
					}
					points.add(points.size()-1, t);
				}
			}

		}

		br.close();

		//if you haven't visited any cell moret than once, then print -1 (x will remain unchanged)
		if(x == Integer.MAX_VALUE) {
			x = -1;
		}
		
		//output
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("mowing.out")));	
		pw.println(x);
		pw.close();

  }
	
	//returns the last index where p is in a
	public static int contains(ArrayList<Point> a, Point p) {
		int x = -1;
		for(int i = 0; i < a.size()-1; i++) {
			if(a.get(i).equals(p)) {
				x = i;
			}
		} 
		return x;
	}

}

//represents a Point
class Point {

	int x;
	int y; 

	public Point(int a, int b) {
		x = a;
		y = b;
	}

	public boolean equals(Point other) {
		if (this.x == other.x && this.y == other.y) {
			return true;
		}
		return false;
	}

	public String toString() {
		return "(" + x + ", " + y + ")";
	}

}