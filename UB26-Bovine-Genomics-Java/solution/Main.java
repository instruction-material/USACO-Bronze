import java.util.*;
import java.io.*;

class Main {
  public static void main(String[] args) throws IOException {
    
		BufferedReader br = new BufferedReader(new FileReader("cownomics.in"));
		StringTokenizer s = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(s.nextToken()); //total number of each type of cow
		int m = Integer.parseInt(s.nextToken()); //total number of positions

		String[] data = new String[n*2];
		for(int i = 0; i < data.length; i++) {
			data[i] = br.readLine();
		}
		br.close();

		int positions = 0;

		//go through each of the positions
		for(int mm = 0; mm < m; mm++) {

			//HashSets of the spotty and plain columns at position mm
			HashSet<Character> spotty = new HashSet<Character>();
			HashSet<Character> plain = new HashSet<Character>();

			//spotty cows [0-n)
			for(int nn = 0; nn < n; nn++) {
				spotty.add(data[nn].charAt(mm));
			}
			//plain cows [n-2n)
			for(int nn = n; nn < n*2; nn++) {
				plain.add(data[nn].charAt(mm));
			}

			//you can't determine spottiness if A, T, C, or G are in both plain and spotty cows
			if(!(plain.contains('A') && spotty.contains('A') 
			|| plain.contains('C') && spotty.contains('C') 
			|| plain.contains('T') && spotty.contains('T') 
			|| plain.contains('G') && spotty.contains('G'))) {
				positions++;
			}

		}
		
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("cownomics.out")));
		pw.println(positions);
		pw.close();

  }
}