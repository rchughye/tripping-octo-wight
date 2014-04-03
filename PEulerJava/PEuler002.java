public class Main {

	/**  Euler Problem #2: Even Fibonacci numbers
		# http://projecteuler.net/problem=2
		# Q: By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
		# A: 4613732
		
		# There is a pattern of odd and even values in the sequence
		# o, e, o, o, e, o, o, e ...
		# starting from the second number, every 3rd value afterwards is even.
		# so 2, 5, 8, 11 ... -> 2 + 3n are even for n = 0, 1 ,2 ...
		
		# Attempt via 'brute force': iterate through all Fibonacci numbers < 4 million then sum every 2 + 3n element
		
		# initialize
	 * 
	 * @param args
	 * no args are used
	 */
	
	
	public static void main(String[] args) {
		// Initialize Variables
		int F_old = 1;
		int F_new = 2;
		int temp = 1;
		int F_element = 2;
		int F_sum = 2;
		
		while (F_new <= 4000000){
			// iterate through Fibonacci sequence
			temp = F_new;
			F_new += F_old;
			F_old = temp;
			F_element += 1;
			
			if (F_element % 3 == 2)
				F_sum += F_new;
		}
		


		System.out.println(F_sum);

	}
