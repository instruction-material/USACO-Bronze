import java.util.*;
import java.io.*;

class Main {
  public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new FileReader("teleport.in"));
		StringTokenizer s = new StringTokenizer(br.readLine());
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("teleport.out")));		
		
		//input
		int a = Integer.parseInt(s.nextToken()); //start pos
		int b = Integer.parseInt(s.nextToken()); //end pos
		int x = Integer.parseInt(s.nextToken()); //teleport x
		int y = Integer.parseInt(s.nextToken()); //teleport y

		//Option 1. Go directly

		int direct = Math.abs(a-b);

		//Option 2. Use teleporter from x to y

		int teleportXY = Math.abs(a-x) + Math.abs(b-y);
		
		//Option 3. Use teleporter from y to x

		int teleportYX = Math.abs(a-y) + Math.abs(b-x);

		//output the minimum of the three travel distances
		pw.println(Math.min(direct, Math.min(teleportXY, teleportYX)));
		
		br.close();
		pw.close();

  }
}