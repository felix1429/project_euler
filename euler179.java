import java.util.*;

public class euler179 {

	public static ArrayList<Integer> getDivisors(int input) {
		
		ArrayList<Integer> divisors = new ArrayList<Integer>();
		
		for(int count = 1;count < Math.pow(input, .5);count ++) {
			if(input / count == (int) (input / count)) {
				divisors.add(count);
				if(input / count != count) {
					divisors.add(input / count);
				}
			}
		}
		return divisors;
	}
	
	public static void main(String [] args) {
		
		int total = 0;
		ArrayList<Integer> temp = new ArrayList<Integer>();
		ArrayList<Integer> notTemp = new ArrayList<Integer>();
		temp.add(1);
		temp.add(2);
		
		for(int counter = 2;counter < 10000000;counter ++) {
			//System.out.println(counter);
			notTemp = getDivisors(counter + 1);
			if((temp.size() == notTemp.size())) {
				total ++;
			}
			temp = notTemp;
		}
		System.out.println(total);
	}
}
