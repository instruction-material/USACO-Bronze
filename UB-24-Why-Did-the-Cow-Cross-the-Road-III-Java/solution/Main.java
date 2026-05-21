import java.util.*;
import java.io.*;

class Main {
  public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new FileReader("cowqueue.in"));
		int cows = Integer.parseInt(br.readLine());
		
		//stores the time data
		Map<Integer, Integer> times = new HashMap<>();
		for(int i = 0; i < cows; i++) {
		
			StringTokenizer st = new StringTokenizer(br.readLine());
			int key = Integer.parseInt(st.nextToken());

			//if another cow already comes to the farm at this time, then add the waiting time for this cow to the waiting time for the other cow
			if (times.containsKey(key)) {
				times.put(key, Integer.parseInt(st.nextToken()) + times.get(key));
			//otherwise just put in a new time entry for this cow
			} else {
				times.put(key, Integer.parseInt(st.nextToken()));
			}

		}

		//sorts the keys of the HashMap in a separate ArrayList which you can use to access the values
		List<Integer> keys = new ArrayList<>(times.keySet());
		Collections.sort(keys);

		int current = 0; //keeps track of the current time

		for(int i = 0; i < keys.size(); i++) {
			
			int key = keys.get(i);
			int value = times.get(key);
			
			//if you haven't reached the time at which the next cow enters, then skip forward to that time (key)
			if(key > current) {
				current = key;
			}
			//increase time by how long it takes for the cow to get questioned (value)
			current += value;

		}

		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("cowqueue.out")));
		pw.println(current);
		pw.close();
		br.close();

  }
}