/*
ID: irith1
LANG: JAVA
TASK: friday
*/

import java.io.*;
import java.util.*;

class Main {
  public static void main(String[] args) throws IOException {
    
		// read input
		BufferedReader br = new BufferedReader(new FileReader("friday.in"));
		int input = Integer.parseInt(br.readLine());
		br.close();

		// 1/1/1900 was a Monday
		int day = 0;
		
		// dayOfWeek stores the number of 13ths that fell on each day of the week
		int[] dayOfWeek = new int[7];
		
		int[] daysInMonth = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

		// loop through years
		for(int year = 1900; year <= 1900+input-1; year++) {

			// loop through months
			for(int month = 0; month < 12; month++) {

				// change numDaysInMonth if it is a leap year
				int numDaysInMonth = daysInMonth[month];
				
				if(month == 1){ // if it is February
				
					if(year % 100 == 0){ // if the year is a century
				
						if(year % 400 == 0){ // if the year is divisible by 400
				
							numDaysInMonth += 1; // leap year

						}
				
					} else if(year % 4 == 0){ // if the year is not a century and divisible by 4
					
						numDaysInMonth += 1; // leap year
				
					}
				
				}

				// loop through dates
				for(int date = 1; date<= numDaysInMonth; date++) {

					// update dayOfWeek when date is the 13th
					if (date == 13) {
						dayOfWeek[day] += 1; 
					}

					day++;

          // loop back around from Sun to Mon
					if (day > 6) {
						day = 0;
					}

				}

			}

		}
		
		// write output
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("friday.out")));
		pw.print(dayOfWeek[5] + " ");
		pw.print(dayOfWeek[6] + " ");
		pw.print(dayOfWeek[0] + " ");
		pw.print(dayOfWeek[1] + " ");
		pw.print(dayOfWeek[2] + " ");
		pw.print(dayOfWeek[3] + " ");
		pw.print(dayOfWeek[4]);
		pw.println();
		pw.close();
  }
}