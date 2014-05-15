import java.math.BigInteger;

public class euler25 {
	
	public static BigInteger fib = BigInteger.valueOf(1);
	public static BigInteger fibbey = BigInteger.valueOf(2);
	public static BigInteger fibber;
	
	public static void main(String[] args) {
		
		int count = 3;
		while(true) {
			fibber = fib.add(fibbey);
			fib = fibbey;
			fibbey = fibber;
			count ++;
			if(fibbey.toString().length() == 1000) {
				System.out.println(count);
				break;
			}
		}
	}
}
