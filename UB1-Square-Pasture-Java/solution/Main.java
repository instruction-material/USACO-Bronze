import java.io.*;
import java.util.*;

class Main {
  public static void main(String[] args) throws IOException {

		// read input
		BufferedReader br = new BufferedReader(new FileReader("square.in"));

		int[] arr1 = new int[4];
		StringTokenizer st = new StringTokenizer(br.readLine());

		for (int i = 0; i < 4; i++) {
			arr1[i] = Integer.parseInt(st.nextToken());
		}
		
		int[] arr2 = new int[4];
		st = new StringTokenizer(br.readLine());

		for (int i = 0; i < 4; i++) {
			arr2[i] = Integer.parseInt(st.nextToken());
		}

		br.close();

		// find min and max of x-coordinates
		int minX = Math.min(arr1[0], arr2[0]);
		int maxX = Math.max(arr1[2], arr2[2]);

		// find min and max of y-coordinates
		int minY = Math.min(arr1[1], arr2[1]);
		int maxY = Math.max(arr1[3], arr2[3]);

		// find area
		int xDistance = maxX - minX;
		int yDistance = maxY - minY;
		int sideLength = Math.max(xDistance, yDistance);
		int area = (int)(Math.pow(sideLength, 2));

		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("square.out")));
		pw.println(area);
		pw.close();
  }
}