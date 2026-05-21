/*
ID: your_id_here
LANG: JAVA
TASK: combo
*/

import java.io.*;
import java.util.*;

class Main {
  public static void main(String[] args) throws IOException {

		//retrieve the input data: dial number, FJ's combination,  master combination
		BufferedReader br = new BufferedReader(new FileReader("combo.in"));
		int num = Integer.parseInt(br.readLine());
		StringTokenizer s = new StringTokenizer(br.readLine());
		Code code1 = new Code(Integer.parseInt(s.nextToken()), Integer.parseInt(s.nextToken()), Integer.parseInt(s.nextToken()));
		s = new StringTokenizer(br.readLine());
		Code code2 = new Code(Integer.parseInt(s.nextToken()), Integer.parseInt(s.nextToken()), Integer.parseInt(s.nextToken()));

		//all valid codes are stored in this ArrayList
		ArrayList<Code> a = new ArrayList<Code>();
		
		for(int i = 0; i < 2; i++) { //code1 = 0; code2 = 1
			for(int j = -2; j <= 2; j++) { //difference in x
				for(int k = -2; k <= 2; k++) { //difference in y
					for(int l = -2; l <= 2; l++) { //difference in z
          
						//you have to test if the combination is valid with both code1 and code2
						//add new code with added difference (j, k, l) to ArrayList

						if(i == 0) { //code1

							Code c = new Code(code1.x + j, code1.y + k, code1.z + l);
							add(a, c, num);

						} else { //code2

							Code c = new Code(code2.x + j, code2.y + k, code2.z + l);
							add(a, c, num);

						}
					}
				}
			}
		}

		//output
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("combo.out")));	
		pw.println(a.size());
		pw.close();
		br.close();

  }

	//adds the combination to ArrayList a
	public static void add(ArrayList<Code> a, Code c, int num) {

		//fix the code to make it loop back around if it is negative or above num
		
		//x, y, or z is negative
		if(c.x <= 0) {
			c.x = num + c.x;
		}
		if(c.y <= 0) {
			c.y = num + c.y;
		}
		if(c.z <= 0) {
			c.z = num + c.z;
		}

		//x, y, or z is above num
		if(c.x > num) {
			c.x = c.x-num;
		}
		if(c.y > num) {
			c.y = c.y-num;
		}
		if(c.z > num) {
			c.z = c.z-num;
		}

		//check if the combination hasn't already been added in the ArrayList
		boolean found = false;
		for(int i = 0; i < a.size(); i++) {
			if(a.get(i).equals(c)) {
				found = true;
			}
		}

		//only add combination if x, y, and z are in bounds and if the combination hasn't already been added
		//NOTE that even though x, y, and z were looped back around, they could still be out of bounds if num is a super small number (such as 1)
		if(!found && c.x > 0 && c.y > 0 && c.z > 0 && 
		c.x <= num && c.y <= num && c.z <= num) {
			a.add(c);
		}

	}

}

//code class represents a combination of ints (x, y, z)
class Code {

	int x;
	int y;
	int z;

	public Code(int i, int j, int k) {
		x = i;
		y = j;
		z = k;
	}

	//method to check if two codes are equal: their x, y, and z values are the same
	public boolean equals(Code other) {
		if(this.x == other.x && this.y == other.y && this.z == other.z) {
			return true;
		}
		return false;
	}

	public String toString() {
		return x + " " + y + " " + z;
	}

}