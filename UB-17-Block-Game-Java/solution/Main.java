import java.util.*;
import java.io.*;

class Main {
  public static void main(String[] args) throws IOException {
    
		int[] letters = new int[26];

		//input
		BufferedReader br = new BufferedReader(new FileReader("blocks.in"));			
		int boards = Integer.parseInt(br.readLine());
		
		for(int x = 0; x < boards; x++) { //for each word pair
			
			StringTokenizer st = new StringTokenizer(br.readLine());
			String word1 = st.nextToken();
			String word2 = st.nextToken();
			int[] word1Letters = new int[26];
			int[] word2Letters = new int[26]; 

			//get letters in word1 and word2 by incrementing the number at the appropriate index (using ASCII)
			for(int i = 0; i < word1.length(); i++) {
				word1Letters[(int)word1.charAt(i) - 97]++;
			}
			for(int i = 0; i < word2.length(); i++) {
				word2Letters[(int)word2.charAt(i) - 97]++;
			}

			//put this data into letters by getting the max of the frequencies in word1 and word2
			for(int i = 0; i < letters.length; i++) {
				letters[i] += Math.max(word1Letters[i], word2Letters[i]);
			}

		}

		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("blocks.out")));

		//print out each frequency in letters
		for(int i = 0; i < 26; i++) {
			pw.println(letters[i]);
		}

		br.close();
		pw.close();

  }

}