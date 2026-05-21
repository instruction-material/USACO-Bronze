import java.util.*;
import java.io.*;

class Main {
  public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new FileReader("speeding.in"));
		StringTokenizer s = new StringTokenizer(br.readLine());
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("speeding.out")));

		int n = Integer.parseInt(s.nextToken()); //input road
		int m = Integer.parseInt(s.nextToken()); //input bessie
		
		int[] road = new int[100]; //index is the mile and value is the speed
		int current = 0; //current mile on the road
		
		//fill road array with speed limits for each mile
		for(int i = 0; i < n; i++) {

			s = new StringTokenizer(br.readLine());
			
			//end = the end of the current road segment
			//speed = speed limit for this segment
			int end = Integer.parseInt(s.nextToken()) + current;
			int speed = Integer.parseInt(s.nextToken());
			
			//segment goes from current to end
			for(int x = current; x < end; x++) {
				road[x] = speed; //fill road array with speed limit
			}
			current = end; //update the current mile
			
		}
		
		int bessie = 0; //bessie's current mile on the road
		int max = 0; //max above speed limit

		//go through bessie's driving journey
		for(int i = 0; i < m; i++) {
			
			s = new StringTokenizer(br.readLine());

			//end = the end of the current segment
			//speed = speed bessie is driving at on this segment 
			int end = Integer.parseInt(s.nextToken()) + bessie;
			int speed = Integer.parseInt(s.nextToken());

			//segment goes from bessie to end
			for(int x = bessie; x < end; x++) {
				
				//if bessie's speed is above speed limit and if the amount bessie is driving above speed limit is greater than max, then update max
				if(speed > road[x] && speed-road[x] > max) {
					max = speed-road[x];
				} 

			}
			bessie = end; //update the mile that bessie is on

		}

		pw.println(max); //output

		br.close();
		pw.close();

  }
}