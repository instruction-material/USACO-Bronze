import java.util.*;
import java.io.*;

class Main {
  public static void main(String[] args) throws IOException {
    
		BufferedReader br = new BufferedReader(new FileReader("bcs.in"));
		PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("bcs.out")));	

		StringTokenizer s = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(s.nextToken()); //size of piece
		int k = Integer.parseInt(s.nextToken()); //number of pieces

		//originalPiece stores the original piece as 2D array of characters (. or #)
		char[][] originalPiece = new char[n][n];
		for(int i = 0; i < n; i++) {
			String row = br.readLine();
			for(int j = 0; j < n; j++) {
				originalPiece[i][j] = row.charAt(j);
			}
		}

		//pieces is an array of 2D arrays, where each 2D array is a piece
		char[][][] pieces = new char[k][n][n];
		for(int p = 0; p < k; p++) {
			for(int i = 0; i < n; i++) {
				String row = br.readLine();
				for(int j = 0; j < n; j++) {
					pieces[p][i][j] = row.charAt(j);
				}
			}
		}

		br.close();

		//loop through each pair of pieces
		for(int index1 = 0; index1 < k; index1++) {
			for(int index2 = 0; index2 < k; index2++) {
				if(index1 != index2) {
					
					//get the pair of pieces
					char[][] piece1 = pieces[index1];
					char[][] piece2 = pieces[index2];

					//get boundaries for each piece
					int[] bounds1 = findBoundaries(piece1);
					int[] bounds2 = findBoundaries(piece2);

					//check each shifted version of each piece against the other
					for(int dx1 = -bounds1[0]; dx1 < n-bounds1[1]; dx1++) {
						for(int dy1 = -bounds1[2]; dy1 < n-bounds1[3]; dy1++) {
							for(int dx2 = -bounds2[0]; dx2 < n-bounds2[1]; dx2++) {
								for(int dy2 = -bounds2[2]; dy2 < n-bounds2[3]; dy2++) {
									char[][] newPiece1 = shift(piece1, dx1, dy1);
									char[][] newPiece2 = shift(piece2, dx2, dy2);
									//check if the pieces, if superimposed on each other, make up the original piece
									if(checkFit(newPiece1, newPiece2, originalPiece)) {
										//output the answer
										pw.println((index1+1) + " " + (index2+1));
										pw.close();
										return;
									}
								}
							}
						}
					}

				}
			}
		}

		pw.close();

  }

	//returns true if the two pieces (p1 and p2) create the original piece (og) when superimposed
	public static boolean checkFit(char[][] p1, char[][] p2, char[][] og) {
		//make a copy of p1 called pNew
		//pNew represents the combination of p1 and p2
		char[][] pNew = new char[p1.length][p1.length];
		for(int i = 0; i < p1.length; i++) {
			for(int j = 0; j < p1.length; j++) {
				pNew[i][j] = p1[i][j];
			}
		}
		//superimpose p2 onto p1
		for(int i = 0; i < p1.length; i++) {
			for(int j = 0; j < p1.length; j++) {
				//if both p1 and p2 have a '#', then return false
				if(pNew[i][j] == '#' && p2[i][j] == '#') {
					return false;
				//if p2 has a '#' that p1 doesn't have, add it to p1
				} else if(p2[i][j] == '#') {
					pNew[i][j] = '#';
				}
			}
		}
		//return whether or not pNew equals the original piece
		return equal(pNew, og);
	}

	//returns the boundaries of piece p - where the # exists
	public static int[] findBoundaries(char[][] p) {
		//variables representing boundaries
		int minX = p.length;
    int maxX = 0;
    int minY = p.length;
    int maxY = 0;
		//find boundaries
    for(int i = 0; i < p.length; i++) {
			for(int j = 0; j < p.length; j++) {
				if(p[i][j] == '#') {
					minX = Math.min(minX, i);
					maxX = Math.max(maxX, i);
					minY = Math.min(minY, j);
					maxY = Math.max(maxY, j);
				}
			}
		}
		int[] boundaries = {minX, maxX, minY, maxY};
		return boundaries;
	}

	//return the shifted version of piece p; a shift is represented by dx and dy
	public static char[][] shift(char[][] p, int dx, int dy) {
		char[][] newP = new char[p.length][p.length];
		//initially sets everything to '.'
		for(int i = 0; i < p.length; i++) {
			for(int j = 0; j < p.length; j++) {
				newP[i][j] = '.'; 
			}
		}
		//adds '#' in appropriate places
		for(int i = 0; i < p.length; i++) {
			for(int j = 0; j < p.length; j++) {
				if(p[i][j] == '#') { 
					newP[i+dx][j+dy] = '#';
				}
			}
		}
		return newP;
	}

	//checks if two 2D arrays are equal (i.e. they have the same characters in each spot)
	public static boolean equal(char[][] a, char[][] b) {
		for(int i = 0; i < a.length; i++) {
			for(int j = 0; j < a[0].length; j++) {
				if(a[i][j] != b[i][j]) {
					return false;
				}
			}
		}
		return true;
	}
}