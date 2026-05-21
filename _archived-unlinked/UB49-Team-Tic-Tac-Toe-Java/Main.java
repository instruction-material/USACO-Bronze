import java.util.*;
import java.io.*;

class Main {
  public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new FileReader("tttt.in"));
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("tttt.out")));	

		char[][] board = new char[3][3];

		for(int i = 0; i < 3; i++) {
      String s = br.readLine();
      for(int j = 0; j < 3; j++) {
        board[i][j] = s.charAt(j);
      }
		}

    int ans1 = 0;
    int ans2 = 0;
    
    // Loop through all teams
    for(int i = 0; i < 26; i++) {
      ans1 += checkWin(board, (char)('A' + i), '-');
      for(int j = i + 1; j < 26; j++) {
        ans2 += checkWin(board, (char)('A' + i), (char)('A' + j));
      }
    }

		pw.println(ans1);
    pw.println(ans2);

		br.close();
		pw.close();

  }

	// returns whether team formed by poss1 and poss2 can win
	public static int checkWin(char[][] board, char poss1, char poss2) {
    boolean canWin = false;
    for(int i = 0; i < 3; i++) {
      char[] row = board[i];
      canWin = canWin || check(row, poss1, poss2);

      char[] col = {board[0][i], board[1][i], board[2][i]};
      canWin = canWin || check(col, poss1, poss2);
    }
    char[] diag = {board[0][0], board[1][1], board[2][2]};
    canWin = canWin || check(diag, poss1, poss2);

    char[] diag2 = {board[0][2], board[1][1], board[2][0]};
    canWin = canWin || check(diag2, poss1, poss2);
    return canWin ? 1 : 0;
	}

  // returns whether a single set of three chars can be claimed a win by poss1 and poss2
  public static boolean check(char[] cows, char poss1, char poss2) {
    boolean exist1 = false;
    boolean exist2 = poss2 == '-';
    for(int i = 0; i < 3; i++) {
      if(cows[i] != poss1 && cows[i] != poss2) {
        return false;
      }
      exist1 = exist1 || (cows[i] == poss1);
      exist2 = exist2 || (cows[i] == poss2);
    }
    return exist1 && exist2;
  }
}