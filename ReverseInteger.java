/*
 * Question:
 * Reverse digits of an integer.
 * 
 * Example1: x = 123, return 321
 * Example2: x = -123, return -321
 */
public class ReverseInteger {
	public int reverseInteger(int x){
		try{
			boolean nag = x<0? true:false;
			String s = "" + Math.abs(x);
			char[] ca = s.toCharArray();
			s = "";
			for(int i = 0; i < ca.length; i++){
				s += ca[ca.length-1-i];
			}
			s = nag? "-"+s : s;
			return Integer.parseInt(s);
		}catch(Exception e){
			return 0;
		}
	}

}
