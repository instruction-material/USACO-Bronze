import java.util.*;
import java.io.*;

class Main {
  public static void main(String[] args) throws IOException {
    
		BufferedReader br = new BufferedReader(new FileReader("lifeguards.in"));

		//cows is the total number of lifeguards
		int cows = Integer.parseInt(br.readLine());
		
		//lifeguards is a HashMap that contains the start time and end time of each lifeguard
		HashMap<Integer, Integer> lifeguards = new HashMap<Integer, Integer>();

		//initialize the lifeguards HashMap
		for(int i = 0; i < cows; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int startTime = Integer.parseInt(st.nextToken());
			int endTime = Integer.parseInt(st.nextToken());
			lifeguards.put(startTime, endTime);
		}

		//sort the HashMap using an ArrayList of sorted keys
		ArrayList<Integer> sortedKeys = new ArrayList<>(lifeguards.keySet());
		Collections.sort(sortedKeys);

		int maxTime = 0; //answer

		//we are firing the lifeguard at index i
		for(int i = 0; i < sortedKeys.size(); i++) {

			int time = 0; //total time covered by lifeguards
			int current = 0; //current time we are at

			for(int j = 0; j < sortedKeys.size(); j++) {
				
				if(i != j) { //count time for all lifeguards except the one you fired (at index i)

					//get start and end times
					int start = sortedKeys.get(j);
					int end = lifeguards.get(start);
					
					//CASE 1: If the start time is past the current time, then add (end - start) to time; in other words, the lifeguard's shift
					
					//CASE 2: If we have already past the start time, then add (end - current) to time; in other words, the time that it takes to get to end

					if(start > current) {
						time += (end - start); //CASE 1
					} else {
						time += (end - current); //CASE 2
					}
					current = end; //update the current time

				}

			}

			//update maxTime 
			if(time > maxTime) {
				maxTime = time;
			}

		}

		//output
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("lifeguards.out")));
		pw.println(maxTime);
		pw.close();

  }
}