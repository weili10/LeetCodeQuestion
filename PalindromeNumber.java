/**
 * Question:Determine whether an integer is a palindrome. Do this without extra space.
 * 
 * @author liwei
 *
 */
public class PalindromeNumber {
	public boolean isPalindrome(int x) {
		if(x < 0){
			x = -x;
		}
        String s = Integer.toString(x);
        System.out.println(s);
        int l = s.length();
        for(int i = 0; i <= l/2; i++){
        	if(s.charAt(i) != s.charAt(l-i-1)){
        		return false;
        	}
        }
        return true;
    }
}
