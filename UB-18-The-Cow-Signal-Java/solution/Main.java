import java.io.*;
import java.util.*;

class Main {
  public static void main(String[] args) throws IOException {
    
		//input m, n, and k
		BufferedReader br = new BufferedReader(new FileReader("cowsignal.in"));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int m = Integer.parseInt(st.nextToken());
		int n = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("cowsignal.out")));

		//output an enlarged symbol
		for(int i = 0; i < m; i++) { //for each line
			String line = br.readLine(); //current line
			for(int z = 0; z < k; z++) { //repeat it k times
				for(int j = 0; j < n; j++) { //for each character
					for(int x = 0; x < k; x++) { //repeat it k times
						pw.print(line.charAt(j)); //print character
					}
				}
				pw.println(); //enter for new line
			}
		}
		br.close();
		pw.close();

  }
}