import java.util.*;
import java.io.*;

class Main {
	public static void main (String [] args) throws IOException {
		
    // read input
		BufferedReader br = new BufferedReader(new FileReader("gift1.in"));
		int people = Integer.parseInt(br.readLine());
		String[] arr = new String[people];
		
		// money is a HashMap, where the key is the person's name, and the value is the amount of money the person has
		HashMap<String, Integer> money = new HashMap<String, Integer>();

		// setup array of people and initialize money
		for (int i = 0; i < people; i++) {
			String name = br.readLine();
			arr[i] = name;
			money.put(name, 0);
		}

		// loop through the different people
		for(int i = 0; i < people; i++) {

			String current = br.readLine(); // current name

			StringTokenizer st = new StringTokenizer(br.readLine());
			int moneyAmt = Integer.parseInt(st.nextToken());
			int numPeople = Integer.parseInt(st.nextToken());

			if(numPeople != 0) {
				// for the current person:
				// the amount of money in their account will be whatever they have in their account currently, minus the amount of money they gave away, plus any leftover money after the division
				// amount they have currently = money.get(current)
				// money they gave away = moneyAmt
				// leftover money = moneyAmt % numPeople = remainder
				money.put(current, money.get(current) - moneyAmt + (moneyAmt%numPeople));

				// this for loop goes through all of the people receiving money
				for(int j = 0; j < numPeople; j++) {
					String receiver = br.readLine();
					// for the receiver:
					// the amount of money in their account will be whatever they have in their account currently, plus the part of the money they are getting
					// money they have currently = money.get(receiver)
					// money they get = moneyAmt / numPeople
					money.put(receiver, money.get(receiver) + (moneyAmt / numPeople));
				}

			}

		}

		br.close();

		// write output
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("gift1.out")));
		for(int x = 0; x < people; x++) {
			pw.print(arr[x] + " ");
			pw.print(money.get(arr[x]));
			pw.println();
		}
		pw.close();

	}
}