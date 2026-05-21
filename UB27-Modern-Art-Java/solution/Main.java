import java.util.*;
import java.io.*;

class Main {
  public static void main(String[] args) throws IOException {
    
		BufferedReader br = new BufferedReader(new FileReader("art.in"));
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("art.out")));		

		//stores all colors that could possibly be first
		ArrayList<Integer> a = new ArrayList<Integer>();
		
		int length = Integer.parseInt(br.readLine());
		int[][] painting = new int[length][length];
		
		//initialize painting and put all of the colors in the painting in ArrayList a
		for(int i = 0; i < length; i++) {
			String s = br.readLine();
			for(int j = 0; j < length; j++) {
				painting[i][j] = Character.getNumericValue(s.charAt(j));
				//if the color is not of the blank canvas and is not already in ArrayList a, then add it to a
				if(painting[i][j] != 0 && !value(a, painting[i][j])) {
					a.add(painting[i][j]);
				}
			
			}
		}
		br.close();

		//loop through each of the colors
		for(int color = 1; color <= 9; color++) {
			
			//represent the rectangle of color
			int minX = length;
			int maxX = 0;
			int minY = length;
			int maxY = 0;

			//find minX, maxX, minY, and maxY
			for(int i = 0; i < length; i++) {
				for(int j = 0; j < length; j++) {
					
					if(painting[i][j] == color) {
						if(i < minX) {
							minX = i;
						}
						if(i > maxX) {
							maxX = i;
						}
						if(j < minY) {
							minY = j;
						}
						if(j > maxY) {
							maxY = j;
						}
					}

				}
			}

			//loop through rectangle of color
			for(int i = minX; i <= maxX; i++) {
				for(int j = minY; j <= maxY; j++) {
					
					//if the color at that spot is not equal to color and if it isn't just the blank canvas
					if(painting[i][j] != color && 
					painting[i][j] != 0) {
						//painting[i][j] is over color and cannot be painted first
						remove(a, painting[i][j]);
					}

				}
			}

		}

		//a.size() is the number of colors that could've been painted first
		pw.println(a.size());
		pw.close();

	}
	
	//returns true if int i is in ArrayList a
	public static boolean value(ArrayList<Integer> a, int i) {
		for(int x = 0; x < a.size(); x++) {
			if(a.get(x) == i) {
				return true;
			}
		}
		return false;
	}
	
	//removes int i from ArrayList a
	public static void remove(ArrayList<Integer> a, int i) {
	
		for(int x = 0; x < a.size(); x++) {
			if(a.get(x) == i) {
				a.remove(x);
			}
		}
	
	}

}