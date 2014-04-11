import java.util.*;

public class euler36 {
	
	static Scanner sc = new Scanner(System.in);
	static Integer total = 0;
	static String palindromeStr;
	static String scanInput;
	static String binaryStr;
	
	private static String isPalindrome(String input) {
		Integer strLength = input.length();
		String firstHalf;
		String secondHalf;
		String secondHalfReverse;
		
		if(strLength % 2 == 0) {
			firstHalf = input.substring(0, (strLength / 2));
			secondHalf = input.substring(strLength / 2);
			secondHalfReverse = new StringBuilder(secondHalf).reverse().toString();
		}else {
			firstHalf = input.substring(0, ((strLength - 1) / 2));
			secondHalf = input.substring(((strLength + 1) / 2));
			secondHalfReverse = new StringBuilder(secondHalf).reverse().toString();
		}
		
		if(firstHalf.equals(secondHalfReverse)) {
			return input;
		}else {
			return "n";
		}
	}
	
	public static void main(String args[]) {
		
		for(Integer counter = 1;counter < 1000000;counter ++) {
			palindromeStr = isPalindrome(counter.toString());
			if(palindromeStr != "n") {
				binaryStr = Integer.toBinaryString(Integer.parseInt(palindromeStr));
				palindromeStr = isPalindrome(binaryStr);
				if(palindromeStr != "n") {
					total += counter;
				}
			}
		}
		System.out.println(total);
	}
}
