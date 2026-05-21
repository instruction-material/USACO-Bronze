/*
ID: roobeelee
LANG: JAVA
TASK: milk
*/

import java.util.*;
import java.io.*;

class milk {
  public static void main(String[] args) throws IOException {
    
		BufferedReader br = new BufferedReader(new FileReader("milk.in"));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int price = 0; 
		int totalUnits = Integer.parseInt(st.nextToken());
		int numFarmers = Integer.parseInt(st.nextToken());

		TreeMap<Integer, Integer> priceUnits = new TreeMap<Integer, Integer>();

		for(int i = 0; i < numFarmers; i++) {
			st = new StringTokenizer(br.readLine());
			int key = Integer.parseInt(st.nextToken());
			
      // if the TreeMap already has this price, update the number of units available at this price, otherwise put this info into the TreeMap
			if (priceUnits.containsKey(key)) {
				priceUnits.put(key, Integer.parseInt(st.nextToken()) + priceUnits.get(key));
			} else {
				priceUnits.put(key, Integer.parseInt(st.nextToken()));
			}
		}

    br.close();

		// loop through TreeMap in ascending order looping through the entrySet is more performant than looping through the keySet()
		for (Map.Entry<Integer, Integer> entry : priceUnits.entrySet()) {
      int pricePoint = (int)entry.getKey();
      int availableUnits = (int)entry.getValue();

      // we either need to buy all of the units available at this price, or buy the amount we need to satisfy the total and break
			if (availableUnits < totalUnits) {
				totalUnits -= availableUnits; 
				price += pricePoint * availableUnits;
			} else {
				price += pricePoint * totalUnits;
				break;
			}
		}

    // write output
    PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("milk.out")));
		pw.println(price);
		pw.close();

  }
}
