import java.util.HashSet;
/**Question: Given a string, find the length of the longest substring 
 *           without repeating characters.
 * Example:Given "abcabcbb", the answer is "abc", which the length is 3.
 *         Given "bbbbb", the answer is "b", with the length of 1.
 * 
 * @author liwei
 *
 */
public class lengthOfLongestSubstring {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String s = args[0];
		int maxLength = 0;
		boolean hasRepChar = false;
		HashSet<Character> charSet = new HashSet<Character>();
		
		for(int i = 0; i < s.length(); i++){
			int j = 0;
			hasRepChar = false;
			charSet.clear();
			while(!hasRepChar && (i+j) < s.length()){
				if(charSet.contains(s.charAt(i+j))){
					hasRepChar = true;
					i = s.indexOf(s.charAt(i+j), i);   //decrease and conquer
				}else{
					charSet.add(s.charAt(i+j));
					j++;
				}
			}
			if(j > maxLength){
				maxLength = j;
			}
		}
		System.out.println(maxLength);
	}
}
