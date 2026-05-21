import java.util.*;
import java.io.*;

class Main {
  public static void main(String[] args) throws IOException {
    
		BufferedReader br = new BufferedReader(new FileReader("cbarn.in"));
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("cbarn.out")));	

		//input
		int numRooms = Integer.parseInt(br.readLine());
		int[] rooms = new int[numRooms];
		for(int i = 0; i < numRooms; i++) {
			rooms[i] = Integer.parseInt(br.readLine());
		}

		//get the minimum distance the cows have to travel by greedily testing each door as being the open door
		int minDistance = Integer.MAX_VALUE;
		for(int i = 0; i < numRooms; i++) {
			int distance = calculateDistance(i, rooms);
			minDistance = Math.min(distance, minDistance);
		}

		//output
		pw.println(minDistance);
		br.close();
		pw.close();

  }

	//calculates the amount of distance the cows travel if openDoorNum is opened
	public static int calculateDistance(int openDoor, int[] rooms) {
		int distance = 0;
		for(int i = 0; i < rooms.length; i++) {
			int idealRoom = i;
			int cows = rooms[i];
			//cows go clockwise around the circle; check if they are going around 
			if(idealRoom >= openDoor) {
				distance += (idealRoom - openDoor) * cows;
			} else {
				distance += (rooms.length - openDoor + idealRoom) * cows;
			}
		}
		return distance;
	}
}