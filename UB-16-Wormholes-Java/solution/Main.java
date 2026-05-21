/*
ID: your_id_here
LANG: JAVA
TASK: wormhole
*/

import java.util.*;
import java.io.*;

class Main {
  public static void main(String[] args) throws IOException {
    
		BufferedReader br = new BufferedReader(new FileReader("wormhole.in"));
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("wormhole.out")));
		
		//read in x and y coordinates
		int n = Integer.parseInt(br.readLine());
		int[] x = new int[n];
		int[] y = new int[n];
		for(int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			x[i] = Integer.parseInt(st.nextToken());
			y[i] = Integer.parseInt(st.nextToken());
		}

		int[] partners = generatePartners(x, y);
		int[] nextOnRight = generateNextOnRight(x, y);
		int totalSolutions = recursive(partners, nextOnRight);
		pw.println(totalSolutions);
		br.close();
		pw.close();

  }

	//create list where each element is the partner of wormhole i
	//if unpaired, the partner is -1
	public static int[] generatePartners(int[] x, int[] y) {
			int[] partners = new int[x.length];
			for(int i = 0; i < x.length; i++) {
					partners[i] = -1;
			}
			return partners;
	}

	//create list where each element is the next wormhole to the right of i
	public static int[] generateNextOnRight(int[] x, int[] y){
		int[] nextOnRight = new int[x.length];
		for(int i = 0; i < x.length; i++) {
				nextOnRight[i] = -1;
		}
		for(int i = 0; i < x.length; i++) {
				//loop through each wormhole
			for(int j = 0; j < x.length; j++) {
				//update nextOnRight if wormhole is the closest to the right
				if(x[j] > x[i] && y[i] == y[j]) {
					if(nextOnRight[i] == -1) {
							nextOnRight[i] = j;
					} else if(x[j] - x[i] < x[nextOnRight[i]]-x[i]) {
						nextOnRight[i] = j;
					}
				}
			}	
		}
		return nextOnRight;
	}
	
	//checks whether a given pairing of wormholes results in a cycle
	public static boolean cycleExists(int[] partners, int[] nextOnRight) {
			//try starting at each wormhole and looking for a cycle
			for(int i = 0; i < partners.length; i++) {
					int pos = i;
					
					//at most, try taking N steps (where each step is a teleport + moving to the right)
					for(int j = 0; j < partners.length; j++) {
							//teleport to the partner wormhole
							pos = partners[pos];
							//jump to the next wormhole on the right
							pos = nextOnRight[pos];
							//stop if there's no wormhole to the right
							if(pos == -1) {
									break;
							}
					}

					//if you're still at a wormhole, then there is a cycle
					if(pos != -1) {
							return true;
					}
			}
					
			return false;
	}

	//recursively generate all pairings of wormholes and check if each pairing results in a cycle
	public static int recursive(int[] partners, int[] nextOnRight) {
			int totalSolutions = 0;
			
			//find the first unpaired wormhole
			int unpairedWormholeIndex = 0;
			boolean foundUnpairedWormhole = false;
			for(int i = 0; i < partners.length; i++) {
				if(partners[i] == -1) {
					unpairedWormholeIndex = i;
					foundUnpairedWormhole = true;
					break;
				}

			}

			//if all wormholes are already paired, check if this pairing is valid
				if (!foundUnpairedWormhole) {
						if(cycleExists(partners, nextOnRight)) {
							return 1;
						} else {
							return 0;
						}
				}

				//try pairing this wormhole with all other possible wormholes
				for(int j = unpairedWormholeIndex+1; j < partners.length; j++) {
					if(partners[j] == -1) {
						partners[unpairedWormholeIndex] = j;
						partners[j] = unpairedWormholeIndex;
						totalSolutions += recursive(partners, nextOnRight);
						partners[unpairedWormholeIndex] = -1;
						partners[j] = -1;
					}
				}

			return totalSolutions;
	}
}