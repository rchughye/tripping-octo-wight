import java.io.*;
import java.util.Scanner;

public class PEuler011 {

	/**
# Euler Problem #11: Largest product in a grid
# http://projecteuler.net/problem=11
# Q: What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?
# A: 70600674

# Step 1: Store data
# Save data as a .txt file via copy paste into Notepad. Import and read by line. Convert to integers and array.
# store in form of rownumber = [num1,num2...,num20]
# store all rows into one main array

# Step 2: Iterate through all direction combinations, store greatest product.
	 * @param args
	 * No args used
	 */
	public static void main(String[] args) {
		// Step 1:
		// file import
		int[][] data;
		data = new int[20][20];
		int countRow = 0;
		int countColumn= 0;
		Scanner input = null;

		try{
		input = new Scanner(new File ("p11.txt"));
		
		while (input.hasNextLine()) {
			
			Scanner line = new Scanner(input.nextLine()).useDelimiter(" ");//
			countColumn = 0;
			
			while (line.hasNext()) {
				data[countRow][countColumn] = line.nextInt();
				//System.out.println(data[countRow][countColumn]);
				countColumn ++;
			}
		  
		    countRow ++;
		    //System.out.println("This is Row: " + countRow);
		    }
		}
		
		catch(IOException ioe){
			System.err.println("Some Error: " + ioe.getMessage());
		}
		finally{
			input.close();
		}
		
		// Step 2:
		// Iterate through data; data[i][j] returns value of row i, column j 
		
		// Initialize
		int gProd = 0; // Greatest product found at any particular point
		int tempProd = 0;
		
		// Iterate through Columns
		for(int i = 0; i<17;i++){
			tempProd = 0;
			for (int j = 0; j<20;j++){
				tempProd = data[i][j]*data[i+1][j]*data[i+2][j]*data[i+3][j];
				if (tempProd > gProd)
					gProd = tempProd;
			}
		}
		// Iterate through Rows
		for(int i = 0; i<20;i++){
			tempProd = 0;
			for (int j = 0; j<17;j++){
				tempProd = data[i][j]*data[i][j+1]*data[i][j+2]*data[i][j+3];
				if (tempProd > gProd)
					gProd = tempProd;
			}
		}
		// Iterate through down right Diagonals; equivalent to up left
		for(int i = 0; i<17;i++){
			tempProd = 0;
			for (int j = 0; j<17;j++){
				tempProd = data[i][j]*data[i+1][j+1]*data[i+2][j+2]*data[i+3][j+3];
				if (tempProd > gProd)
					gProd = tempProd;
			}
		}		
		// Iterate through down left Diagonals; equivalent to up right
		for(int i = 0; i<17;i++){
			tempProd = 0;
			for (int j = 3; j<20;j++){
				tempProd = data[i][j]*data[i+1][j-1]*data[i+2][j-2]*data[i+3][j-3];
				if (tempProd > gProd)
					gProd = tempProd;
			}
		}	
		// Output greatest product found
		System.out.println(gProd);
	}

}
