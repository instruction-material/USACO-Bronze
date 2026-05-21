import java.util.*;
import java.io.*;

class Main {
  public static void main(String[] args) throws IOException {
    
		BufferedReader br = new BufferedReader(new FileReader("hps.in"));
		int games = Integer.parseInt(br.readLine());
		int[][] hps = new int[games][2];

		for(int i = 0; i < games; i++) {

			StringTokenizer st = new StringTokenizer(br.readLine());
			hps[i][0] = Integer.parseInt(st.nextToken());
			hps[i][1] = Integer.parseInt(st.nextToken());

		}

		int wins1 = 0; //1 beats 2 beats 3 beats 1
		int wins2 = 0; //3 beats 2 beats 1 beats 3

		for(int i = 0; i < games; i++) {

				if(hps[i][0] == 1 && hps[i][1] == 2) { 
					wins1++; //1 beats 2
				} else if(hps[i][0] == 2 && hps[i][1] == 3) {
					wins1++; //2 beats 3
				} else if(hps[i][0] == 3 && hps[i][1] == 1) {
					wins1++; //3 beats 1
				} else if(hps[i][0] == 1 && hps[i][1] == 3) {
					wins2++; //1 beats 2
				} else if(hps[i][0] == 3 && hps[i][1] == 2) {
					wins2++;
				} else if(hps[i][0] == 2 && hps[i][1] == 1) {
					wins2++;
				}
				//otherwise, it is a tie

		}

		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("hps.out")));
		pw.println(Math.max(wins1, wins2));

		br.close();
		pw.close();
		
  }
}