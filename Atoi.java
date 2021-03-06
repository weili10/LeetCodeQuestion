/**
 * Question:
 * Implement atoi to convert a string to an integer.
 * 
 *  Requirement:
 *  The function first discards as many whitespace characters as necessary until the first non-whitespace character is 
 *  found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many 
 *  numerical digits as possible, and interprets them as a numerical value.
 *  
 *  The string can contain additional characters after those that form the integral number, which are ignored and have 
 *  no effect on the behavior of this function.
 *  
 *  If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence 
 *  exists because either str is empty or it contains only whitespace characters, no conversion is performed.
 *  
 *  If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of 
 *  representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
 * @author liwei
 *
 */

public class Atoi {
    public int myAtoi(String str) {
    	try{
	    	int slen = str.length();
	    	int i = 0;
	    	int sign = 1;
	    	char curr;
	    	double sum = 0;
	    	
	    	while(str.charAt(i) == ' '){
	    		i++;
	    	}
	    	if(str.charAt(i) == '+'){
	    		sign = 1;
	    		i++;
	    	}else if(str.charAt(i) == '-'){
	    		sign = -1;
	    		i++;
	    	}
	    	for(;i < slen;i++){
	    	    curr = str.charAt(i);
	    		if(curr >= '0' && curr <= '9'){
	    			sum = sum*10 + (int)(curr - '0');
	    		}else{
	    			break;
	    		}
	    	}
	    	sum *= sign;
	    	if(sum > Integer.MAX_VALUE){
	    		return Integer.MAX_VALUE;
	    	}else if(sum < Integer.MIN_VALUE){
	    		return Integer.MIN_VALUE;
	    	}
	    	return (int)sum;
    	}catch(Exception e){
    		return 0;
    	}
    }
}
