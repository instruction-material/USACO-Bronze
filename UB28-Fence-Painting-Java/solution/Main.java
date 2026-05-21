import java.util.*;
import java.io.*;

class Main {
  public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new FileReader("paint.in"));
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("paint.out")));
		//bessie's interval
		StringTokenizer s = new StringTokenizer(br.readLine());
		int[] bessie = new int[2];
		bessie[0] = Integer.parseInt(s.nextToken());
		bessie[1] = Integer.parseInt(s.nextToken());
		//john's interval
		s = new StringTokenizer(br.readLine());
		int[] john = new int[2];
		john[0] = Integer.parseInt(s.nextToken());
		john[1] = Integer.parseInt(s.nextToken());

		if(bessie[0] < john[0]) {
			//bessie interval then john interval
			if(bessie[1] < john[0]) {
				//no overlap
				pw.println((john[1] - john[0]) + (bessie[1] - bessie[0]));
			} else {
				//overlap
				if(bessie[1] > john[1]) {
					//john is in between bessie
					pw.println(bessie[1] - bessie[0]);
				} else {
					//normal overlap
					pw.println(john[1] - bessie[0]);
				}
			}
		} else if(bessie[0] > john[0]) {
			//john interval then bessie interval
			if(john[1] < bessie[0]) {
				//no overlap
				pw.println((john[1] - john[0]) + (bessie[1] - bessie[0]));
			} else {
				//overlap
				if(john[1] > bessie[1]) {
					//bessie is in between john
					pw.println(john[1] - john[0]);
				} else {
					//normal overlap
					pw.println(bessie[1] - john[0]);
				}
			}
		} else {
			//bessie and john have equal starting points
			pw.println(Math.max(bessie[1], john[1]) - john[0]);
		}

		br.close();
		pw.close();

	}

}