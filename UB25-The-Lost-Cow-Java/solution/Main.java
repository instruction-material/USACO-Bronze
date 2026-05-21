import java.util.*;
import java.io.*;

class Main {
  public static void main(String[] args) throws IOException {
    
		BufferedReader br = new BufferedReader(new FileReader("lostcow.in"));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int x = Integer.parseInt(st.nextToken()); //where Farmer John is
		int y = Integer.parseInt(st.nextToken()); //where Bessie is
		br.close();

		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("lostcow.out")));

		int currentPos = x; //current position of farmer John
		int distance = 0; //distance traveled
		int max = 9 * Math.abs(x - y); //maximum distance

		for(int i = 0; i < max; i++) {
			
			int nextPos = x + (int)Math.pow(-2, i); //get nextPos using FJ's zig-zag strategy

			if (y >= nextPos && y < currentPos 
			|| y <= nextPos && y > currentPos) {
				
				//you found Bessie!
				distance += Math.abs(y-currentPos);
				pw.println(distance);
				pw.close();
				break;
			
			} else {
			
				//update distance and go to nextPos
				distance+=Math.abs(nextPos-currentPos);
				currentPos = nextPos;
			
			}

		}

  }
}