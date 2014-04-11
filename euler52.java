import java.util.Arrays;

public class euler52 {	
	static Integer counter = 1;
	static char[] numArray;
	
	private static char[] intToCA(Integer input) { //CA is char array		
		char[] tempArray;
		
		tempArray = ("" + input).toCharArray();
		Arrays.sort(tempArray);
		return tempArray;
	}
	
	public static void main(String[] args) {

		while(true) {		
			numArray = intToCA(counter);
			Arrays.sort(numArray);
			if(Arrays.equals(intToCA(counter * 2),numArray)) {
				if(Arrays.equals(intToCA(counter * 3),numArray)) {
					if(Arrays.equals(intToCA(counter * 4),numArray)) {
						if(Arrays.equals(intToCA(counter * 5),numArray)) {
							if(Arrays.equals(intToCA(counter * 6),numArray)) {
								System.out.println(counter);
								break;
							}
						}
					}
				}
			}
			counter ++;
		}
	}
}