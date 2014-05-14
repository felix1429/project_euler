import java.math.BigInteger;

public class euler20 {

	public static BigInteger sum = BigInteger.valueOf(1);
	public static Integer digitSum = 0;
	public static char[] finalSum;
	
	public static void main(String[] args) {
		
		for(int count = 2;count <= 100;count ++) {
			sum = sum.multiply(BigInteger.valueOf(count));
		}
		finalSum = sum.toString().toCharArray();
		for(char iter : finalSum) {
			digitSum += Character.getNumericValue(iter);
		}
		System.out.println(digitSum);
	}
}