public class Main {

	/**
	 * #  Euler Problem #10: Summation of primes
		# http://projecteuler.net/problem=10
		# Q: Find the sum of all the primes below two million.
		# A: 142913828922
		
		# Step 1: Find primes and store them
		# Use the Sieve of Eratosthenes method, iteratively eliminating multiples of the next prime numbers
		# i.e. find all primes in a certain range by eliminating all composite numbers
		
	 * @param args
	 * No args used 
	 */
	
	public static void main(String[] args) {
		// Initialize
		boolean[] Prime_Flags;
		Prime_Flags = new boolean[2000000];
		java.util.Arrays.fill(Prime_Flags, true);
		// let Prime_Flags[i] be the flag for number i+1
		Prime_Flags[0] = false; // #1 is not prime
		long Prime_Sum = 0;
		
		// Mark multiples of primes to be false
		for (int i=1; i<=1416; i++){// up to 1414.2, sqrt of 2 000 000
			if (Prime_Flags[i-1] == true) // if i is prime
				for (int j = i*2; j<=2000000; j += i){
					Prime_Flags[j-1] = false;
				}
			
		}
		
		// Sum all Primes marked as true
		for (int i=1; i<2000000; i++){
			if (Prime_Flags[i] == true){
				Prime_Sum += i+1;
			}
		}
		
		System.out.println(Prime_Sum);
		
	}

}
