/*
 * Question:
 * Given a string s, find the longest palindromic substring in s. 
 * You may assume that the maximum length of s is 1000.
 * 
 * Example:
 * Input: "babad"
 * Output: "bab"
 * Note: "aba" is also a valid answer.
 * 
 * Input: "cbbd"
 * Output: "bb"
 */
public class LongestPalindrome {
	public String longestPalindrome(String s){
		int n = s.length();
		int maxLength = 0;
		int position = 0;
		if(n==1){
			return s;
		}
		for(int i = 0; i < n-maxLength/2; i++){
			int k = 1;
			while(i-k >= 0 && i+k < n && s.charAt(i-k) == s.charAt(i+k)){
				k++;
			}
			if(2*k-1 > maxLength){
				maxLength = 2*k-1;
				position = i-k+1;
			}
			if(i != n-1 &&s.charAt(i) == s.charAt(i+1)){
				int j = 1;
				while(i-j >= 0 && i+1+j < n && s.charAt(i-j) == s.charAt(i+1+j)){
					j++;
				}
				if(2*j > maxLength){
					maxLength = 2*j;
					position = i-j+1;
				}
			}
		}
		return s.substring(position, position+maxLength);
	}
}
