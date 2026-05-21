import java.util.*;
import java.io.*;

class Main {
  public static void main(String[] args) throws IOException {
    
		BufferedReader br = new BufferedReader(new FileReader("family.in"));
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("family.out")));	

    StringTokenizer s = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(s.nextToken());
    String cow1 = s.nextToken();
    String cow2 = s.nextToken();

    HashMap<String, String> parents = new HashMap<String, String>();
		

		for(int i = 0; i < n; i++) {
      s = new StringTokenizer(br.readLine());
			String x = s.nextToken();
      String y = s.nextToken();
      parents.put(y, x);
		}
		
    int count1 = 0;
    int count2 = -1;
    boolean done = false;
    String curCow1 = cow1;
    // loop over all ancestors of cow1
    while(!done) {
      String curCow2 = cow2;
      count2 = 0;

      // loop over all ancestors of cow2
      while(!done) {
        if(curCow1.equals(curCow2)) {
          done = true;
          break;
        }
        if(parents.containsKey(curCow2)) { 
          curCow2 = parents.get(curCow2);
          count2 += 1;
        } else
          break;
      }

      if(done) break;
      if(parents.containsKey(curCow1)) { 
        curCow1 = parents.get(curCow1);
        count1 += 1;
      }
      else
        break;
    }
    if(!done) {
      pw.println("NOT RELATED");
    } else if (count1 == 1 && count2 == 1) {
      pw.println("SIBLINGS");
    } else if (count1 > 1 && count2 > 1){
      pw.println("COUSINS");
    } else {
      if(count1 > count2) {
        //Swap cow1, cow2
        String temp = cow1;
        cow1 = cow2;
        cow2 = temp;

        int temp2 = count1;
        count1 = count2;
        count2 = temp2;
      }
      pw.print(cow1 + " is the ");
      for(int i = 0; i < count2 - 2; i++) 
        pw.print("great-");
      if(count1 == 0 && count2 > 1)
        pw.print("grand-");
      if(count1 == 0) 
        pw.print("mother");
      else 
        pw.print("aunt");
      pw.print(" of ");
      pw.println(cow2);
    }

		br.close();
		pw.close();

  }

}