import java.math.BigInteger;

public class euler56 {

	static Integer sum = 0;
	static Integer maxSum = 0;
	static BigInteger result;
	static char [] resultChar;
	
	public static void main(String[] args) {

		for(BigInteger a = new BigInteger("1");a.compareTo(BigInteger.valueOf(100)) < 0;a = a.add(BigInteger.valueOf(1))) {
			for(Integer b = 1;b < 100;b ++) {
				result = a.pow(b);
				resultChar = result.toString().toCharArray();
				for(char element : resultChar) {
					sum += Character.getNumericValue(element);
				}
				if(sum > maxSum) {
					maxSum = sum;
				}
				sum = 0;
			}
		}
		System.out.println(maxSum);
	}
}
