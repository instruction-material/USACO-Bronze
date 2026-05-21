import java.util.*;
import java.io.*;

class Main {
  public static void main(String[] args) throws IOException {
    
		BufferedReader br = new BufferedReader(new FileReader("hoofball.in"));
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("hoofball.out")));	

		//number of cows = n
		int n = Integer.parseInt(br.readLine());
		int[] cows = new int[n];

		StringTokenizer s = new StringTokenizer(br.readLine());

		//initialize the cows array
		for(int i = 0; i < n; i++) {
			cows[i] = Integer.parseInt(s.nextToken());
		}
		Arrays.sort(cows); //sort cows

		//create an array where the index is the cowIndex and the value is the index of the cow nearest to it
		int[] nearest = new int[n];
		for(int i = 0; i < n; i++) {
			nearest[i] = getNearestCow(i, cows);
		}

		int numBalls = 0; //answer

		//check whether each cow would not receive a ball in which case it would need a ball passed to it to start

		for(int i = 0; i < n; i++) { //i is the cowIndex
			boolean receivesPass = false;
        //check whether cow to the left will pass to it
        if(i > 0) {
            if(nearest[i-1] == i) {
                receivesPass = true;
						}
				}
        //check whether cow to the right will pass to it
        if(i < cows.length-1) {
            if(nearest[i+1] == i) {
                receivesPass = true;
						}
				}
				//if no one passes to it, increment numBalls because a ball needs to be passed to it
        if(!receivesPass) {
					numBalls++;
				}
		}

		//also check for pairs of cows that only pass to each other and do not receive passes from anyone else (need a ball to be passed to each of these pairs)

		for(int i = 0; i < n; i++) { //i is the cowIndex
			if(nearest[i] == i+1 && nearest[i+1] == i) {
				//you found a pair that passes only to each other
				boolean receivesPass = false;
				//check if the left cow in pair receives pass from the left
        if(i > 0 && nearest[i-1] == i) {
					receivesPass = true;
				}
        //check if the right cow in pair receives pass from the right
				if(i < cows.length-2 && nearest[i+2] == i+1) {
					receivesPass = true;
				}
				//if neither cow receives a pass from a cow other than each other, a ball needs to be passed to this pair, so increment numBalls
				if(!receivesPass) {
					numBalls++;
				}
			}

		}

		pw.println(numBalls); //output

		br.close();
		pw.close();

  }

	//returns the index of the nearest cow to cowIndex
	public static int getNearestCow(int cowIndex, int[] cows) {
		//cow is on left edge
		if(cowIndex == 0) {
			return 1;
		}
		//cow is on right edge
		if(cowIndex == cows.length-1) {
			return cows.length-2;
		}
		//get left distance and right distance and if left distance is smaller or equal to right distance, then return the left index; otherwise return the right index
		int leftDistance = cows[cowIndex] - cows[cowIndex-1];
		int rightDistance = cows[cowIndex+1] - cows[cowIndex];
		if(leftDistance <= rightDistance) {
			return cowIndex-1;
		} else {
			return cowIndex+1;
		}
	}
}