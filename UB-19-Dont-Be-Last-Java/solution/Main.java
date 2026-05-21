import java.util.*;
import java.io.*;

class Main {
  public static void main(String[] args) throws IOException {
    
		//Bessie, Elsie, Daisy, Gertie, Annabelle, Maggie, and Henrietta = cows 

		BufferedReader br = new BufferedReader(new FileReader("notlast.in"));
		int num = Integer.parseInt(br.readLine()); //number of entries in the milking log

		//HashMap represents the name of the cow and how much milk they have produced
		HashMap<String, Integer> cows = new HashMap<String, Integer>();
		cows.put("Bessie", 0);
		cows.put("Elsie", 0);
		cows.put("Daisy", 0);
		cows.put("Gertie", 0);
		cows.put("Annabelle", 0);
		cows.put("Maggie", 0);
		cows.put("Henrietta", 0);

		for(int i = 0; i < num; i++) { //go through each entry

			//update cows HashMap
			StringTokenizer st = new StringTokenizer(br.readLine());
			String key = st.nextToken();
			cows.put(key, Integer.parseInt(st.nextToken()) + cows.get(key));

		}

		//find the min value
		int min = Integer.MAX_VALUE;
		for(String name : cows.keySet()) {
			if(cows.get(name) < min) {
				min = cows.get(name);
			}
		}

		//find the second least value
		int second = Integer.MAX_VALUE;
		String secondCow = "";
		for(String name : cows.keySet()) {
			if(cows.get(name) > min && cows.get(name) < second) {
				second = cows.get(name);
				secondCow = name;
			}
		}

		//find the occurences of second
		int ties = 0;
		for(String name : cows.keySet()) {
			if(cows.get(name) == second) {
				ties++;
			}
		}

		//output
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("notlast.out")));
		if(ties == 1) { //only one occurrence of second
			pw.println(secondCow);
		} else { //multiple or no occurrences of second
			pw.println("Tie");
		}
		
		br.close();
		pw.close();
		
  }
}