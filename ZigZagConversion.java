/*
 * Question:
 * The string "PAYPALISHIRING" is written in a zigzag pattern on 
 * a given number of rows like this: (you may want to display this 
 * pattern in a fixed font for better legibility)
 * P   A   H   N
 * A P L S I I G
 * Y   I   R
 * And then read line by line: "PAHNAPLSIIGYIR"
 * Write the code that will take a string and make this conversion 
 * given a number of rows:
 *       string convert(string text, int nRows);
 * convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
 */
public class ZigZagConversion {
	public String convert(String s, int numRows){
		String ans = "";
		int n = s.length();
		if(numRows == 1){
			return s;
		}
		int step = 2*numRows - 2;
		for(int i = 0; i < n; i += step){
			ans = ans + s.charAt(i);
		}
		for(int i = 1; i < numRows-1; i++){
			for(int j = i; j < n; j += step){
				ans = ans + s.charAt(j);
				if(j+step-2*i < n){
					ans = ans + s.charAt(j+step-2*i);
				}
			}
		}
		for(int i = numRows-1; i < n; i+= step){
			ans = ans + s.charAt(i);
		}
		return ans;
	}
}
