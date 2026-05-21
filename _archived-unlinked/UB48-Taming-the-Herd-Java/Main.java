import java.util.*;
import java.io.*;

class Main {
  public static void main(String[] args) throws IOException {
    
		BufferedReader br = new BufferedReader(new FileReader("taming.in"));
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("taming.out")));	

		//1. INPUT

		//number of log entries = n
		int n = Integer.parseInt(br.readLine());
		int[] log = new int[n];

		//initialize log array
		StringTokenizer s = new StringTokenizer(br.readLine());
		for(int i = 0; i < n; i++) {
			log[i] = Integer.parseInt(s.nextToken());
		}

		//2. RETRIEVE LOG

		int[] newLog = retrieveLog(log);

		//3. OUTPUT

		//check for inconsistency
		if(newLog[0] == -1) {
			
			pw.println(-1);
		
		//otherwise calculate minimum and maximum breakouts
		} else {

			//for the minimum number of breakouts, then only the days marked 0 had a breakout (none of the -1 were breakouts)

			int min = 0;
			for(int i = 0; i < n; i++) {
				if(newLog[i] == 0) {
					min++;
				}
			}

			//for the maximum number of breakouts, then every day marked -1 was also a breakout
		
			int max = min;
			for(int i = 0; i < n; i++) {
				if(newLog[i] == -1) {
					max++;
				}
			}

			pw.println(min + " " + max);

		}

		br.close();
		pw.close();

	}

	public static int[] retrieveLog(int[] log) {
		
		//edge case: since we know there was a breakout on day 1, the first entry cannot be greater than 0
		if(log[0] > 0) {
			int[] inconsistent = {-1};
			return inconsistent;
		}
			
		//try to reconstruct the log with the given information
		int[] newLog = new int[log.length];
		for(int i = 0; i < log.length; i++) {
			newLog[i] = -1;
		}

		//there was definitely a breakout on day 1
		newLog[0] = 0;

		//trace through the log backwards
		//everytime we see a nonnegative number, try to trace back the number of breakouts
		for(int i = log.length-1; i >= 0; i--) {
			if(log[i] >= 0) { 
				
				int numBreakouts = log[i];
				for(int j = i; j >= 0; j--) {

					//check for consistency
					if(newLog[j] != -1 && newLog[j] != numBreakouts) {
						int[] inconsistent = {-1};
						return inconsistent;
					} else {
						newLog[j] = numBreakouts;
					}
					//decrement numBreakouts
					numBreakouts--;
					if(numBreakouts < 0) {
						break;
					}

				}

			}

		}

		//check if log and newLog are consistent
		for(int i = 0; i < log.length; i++) {
			if(log[i] != newLog[i] && log[i] != -1) {
				int[] inconsistent = {-1};
				return inconsistent;
			}
		}
		return newLog;
	
	}

}