import java.util.*;
import java.io.*;

class Main {
  public static void main(String[] args) throws IOException {
    
		BufferedReader br = new BufferedReader(new FileReader("badmilk.in"));
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("badmilk.out")));	
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		//n people
		//m milk
		//d entries for who drinks what when
		//s entries for who gets sick when
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		int d = Integer.parseInt(st.nextToken());
		int s = Integer.parseInt(st.nextToken());

		//in each ArrayList you have {milk, person, time}
		ArrayList<ArrayList<Integer>> consumedMilk = new ArrayList<ArrayList<Integer>>();

		for(int i = 0; i < d; i++) {
			st = new StringTokenizer(br.readLine());
			int person = Integer.parseInt(st.nextToken());
			int milk = Integer.parseInt(st.nextToken());
			int time = Integer.parseInt(st.nextToken());
			ArrayList<Integer> a = new ArrayList<Integer>();
			a.add(milk);
			a.add(person);
			a.add(time);
			consumedMilk.add(a);
		}

		//key is the person
		//value is the time that person got sick
		HashMap<Integer, Integer> sickPeople = new HashMap<Integer, Integer>();

		//person and time
		for(int i = 0; i < s; i++) {
			st = new StringTokenizer(br.readLine());
			int person = Integer.parseInt(st.nextToken());
			int time = Integer.parseInt(st.nextToken());
			sickPeople.put(person, time); 
		}

		HashSet<Integer> possibleBadMilk = new HashSet<Integer>();

		for(ArrayList<Integer> data : consumedMilk) {
			
			boolean isBad = true;
			int milk = data.get(0);
			int person = data.get(1);
			int time = data.get(2);

			//1. check if all the people who drank this milk got sick after they drank it (if they got sick at all)
		
			for(ArrayList<Integer> consumedData : consumedMilk) {
				int milkDrank = consumedData.get(0);
				if(milkDrank == milk) {
					int personDrank = consumedData.get(1);
					int timeDrank = consumedData.get(2);
					if(sickPeople.containsKey(personDrank)) {
						int timeSick = sickPeople.get(personDrank);
						if(timeSick <= timeDrank) {
							isBad = false;
						}
					}
				}
			}

			//2. check if everyone who got sick drank that milk
			
			HashSet<Integer> peopleWhoDrankBadMilk = new HashSet<Integer>();
			for(ArrayList<Integer> consumedData : consumedMilk) {
				int milkDrank = consumedData.get(0);
				if(milkDrank == milk) {
					int personWhoDrankBadMilk = consumedData.get(1);
					peopleWhoDrankBadMilk.add(personWhoDrankBadMilk);
				}
			}

			for(int sickPerson : sickPeople.keySet()) {
				if(!peopleWhoDrankBadMilk.contains(sickPerson)) {
					isBad = false;
				}
			}

			if(isBad) {
				possibleBadMilk.add(milk);
			}

		}

		//3. find the number of people who drank each badMilk and take the maximum of these numbers to find the maximum doses of medicine
		
		int maxDoses = 0;
		for(int badMilk : possibleBadMilk) {

			HashSet<Integer> peopleWhoDrankBadMilk = new HashSet<Integer>();
			for(ArrayList<Integer> consumedData : consumedMilk) {
				int milkDrank = consumedData.get(0);
				if(milkDrank == badMilk) {
					int personWhoDrankBadMilk = consumedData.get(1);
					peopleWhoDrankBadMilk.add(personWhoDrankBadMilk);
				}
			}

			maxDoses = Math.max(maxDoses, peopleWhoDrankBadMilk.size());

		}

		pw.println(maxDoses);
		br.close();
		pw.close();

  }
}