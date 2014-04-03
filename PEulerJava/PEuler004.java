public class PEuler004 {

	/**Euler Problem #4: Largest palindrome product
	 * http://projecteuler.net/problem=4
	 * Q: Find the largest palindrome made from the product of two 3-digit numbers.
	 * A: 906609
	 * 
	 * Start at 999 x 999 and work backwards from that, checking if each product is a palindrome
	 * store all palindromes, check maximum of list
	 * 
	 * Checking if a palindome:
	 * Product will necessarily have a maximum of 6 digits (999^2 = 998001)
	 * 
	 * @param args
	 * no args are used
	 */
	
	/** Pal_Checker: int -> boolean
	 Outputs True if an input integer is a palindrome, False otherwise
	 Will currently hardcode for positive integers with 6 digits ONLY as that is the expected size for this question
	 Examples: Pal_Checker(111111) -> true, Pal_Checker(111110) -> false
	*/
	public static boolean PalChecker(int val) {
		int d1 = val / 100000;
	    int d2 = (val % 100000) / 10000;
	    int d3 = (val % 10000) / 1000;
	    int d4 = (val % 1000) / 100;
	    int d5 = (val % 100) / 10;
	    int d6 = (val % 10);
	    if ((d1 == d6) & (d2 == d5) & (d3 == d4)) 
	    	return true;
	    else 
	    	return false;
		
	}
	
	public static void main(String[] args) {
		int max = 0;
		int cur = 0;
		for(int i=999; i>500; i = i-1){
			for(int j=999; j>500; j = j-1){
				cur = i*j;
				if (PalChecker(cur) & (cur > max))
					max = cur;
			}
		}
		System.out.println(max);

	}
	


}
