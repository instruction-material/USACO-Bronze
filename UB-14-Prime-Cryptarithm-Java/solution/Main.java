/*
ID: your_id_here
LANG: JAVA
TASK: crypt1
*/

import java.io.*;
import java.util.*;

class Main {
  public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new FileReader("crypt1.in"));

		int total = Integer.parseInt(br.readLine());
		int[] set = new int[total];
		StringTokenizer s = new StringTokenizer(br.readLine());
		for(int i = 0; i < total; i++) {
			set[i] = Integer.parseInt(s.nextToken());
		}

		int answer = 0; //number of solutions

		//loop through all possible combinations of numbers
		for(int aa = 0; aa < total; aa++) { //a
			for(int bb = 0; bb < total; bb++) { //b
				for(int cc = 0; cc < total; cc++) { //c
					for(int dd = 0; dd < total; dd++) { //d
						for(int ee = 0; ee < total; ee++) { //e
							
							//abc * de
							int a = set[aa];
							int b = set[bb];
							int c = set[cc];
							int d = set[dd];
							int e = set[ee];
							
							//strings represent the two numbers you are multiplying together
							String abc = "" + a + b + c;
							String de = "" + d + e;

							//strings represent partial products
							String pa1 = Integer.parseInt(abc)*e + "";
							String pa2 = Integer.parseInt(abc)*d + "";
							
							//string represents the final product
							String product = Integer.parseInt(abc)*Integer.parseInt(de) + "";

							//this combination of numbers is only a solution if the partial products and the final product contain numbers in the speficied set and if the partial products are three digits and if the final product is 4 digits
							if(inSet(abc, set) && inSet(de, set) && inSet(pa1, set) && inSet(pa2, set) && inSet(product, set) && pa1.length() == 3 && pa2.length() == 3 && product.length() == 4) {
								answer++;
							}

						}
					}
				}
			}	
		}

		//output
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("crypt1.out")));	
		pw.println(answer);
		pw.close();
		br.close();

  }
	
	//checks if the "digits" in str are all in set a
	public static boolean inSet(String str, int[] a) {

		//for every "digit" in str, check if it is one of the numbers in int[] a and return false if the "digit" isn't found in the set

		for(int i = 0; i < str.length(); i++) {

			boolean found = false;
			for(int j = 0; j < a.length; j++) {
				int c = Character.getNumericValue(str.charAt(i));
				if(a[j] == c) {
					found = true;
        }
			}

			if(!found) {
				return false;
			}
      
		}
		return true;
	}

}