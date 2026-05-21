import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new FileReader("angry.in"));
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("angry.out")));

		//n = number of cows
		int n = Integer.parseInt(br.readLine());
		
		//initialize the cows array
		int[] cows = new int[n];
		for(int i = 0; i < n; i++) {
			cows[i] = Integer.parseInt(br.readLine());
		}
		Arrays.sort(cows); //sort cows
		
		int max = 1; //max number of exploded cows
		
		//loop through starting points
		for(int start = 0; start < n; start++) {
			
			//get the left most index
			int leftMostExplosion = getExplosionIndex(cows, start, true);
			
			//get the right most index
			int rightMostExplosion = getExplosionIndex(cows, start, false);
			
			//count = number of hay bales that exploded
			int numExploded = rightMostExplosion - leftMostExplosion + 1;
			
			//update max
			if(numExploded > max) {
				max = numExploded;
			}
		}
		
		//output
		pw.println(max);
		pw.close();

	}
	
	public static int getExplosionIndex(int[] cows, int startIndex, boolean goLeft) {
		
		//currentExplosionIndex = index of cow that is exploding
		int currentExplosionIndex = startIndex;
		
		//currentRadius = current blast radius
		int currentRadius = 1;
		
		//keep exploding as long as you haven't reached either end of the cows array
		while(currentExplosionIndex > 0 && currentExplosionIndex < cows.length-1) {
			
			//keeps track of left (neg) and right (pos)
			int direction = 0;
			if(goLeft) {
				direction = -1;
			}
			else {
				direction = 1;
			}
			
			//nextIndex is the next index to check if the explosion can reach, which starts at the current index
			int nextIndex = currentExplosionIndex;
			
			//check if next index is in between 0 and cows.length
			//check if the next closest hay bale is within the range of the explosion
			while(nextIndex + direction >= 0 && 
			nextIndex + direction < cows.length && 
			Math.abs(cows[nextIndex + direction] - cows[currentExplosionIndex]) <= currentRadius) {
				//if so, then increase nextIndex
				//by direction (1 or -1)
				nextIndex += direction;
			}
			
			//at the end of the while loop nextIndex stores the index of the farthest hay bale that exploded due to the one at currentExplosionIndex exploding
			//if the nextIndex is still equal to the currentExplosionIndex then no hay bales have exploded from the blast so you can break
			if(nextIndex == currentExplosionIndex) {
				break;
			}
			
			//if you don't break out of the loop, then you can update currentExplosionIndex to be nextIndex (so far the farthest index of explosion) 
			//you can also increment currentRadius
			currentExplosionIndex = nextIndex;
			currentRadius++;
		}
		
		//once the while loop breaks, you can return currentExplosionIndex, which stores the farthest index that the explosion reached
		return currentExplosionIndex;
	}
	
}