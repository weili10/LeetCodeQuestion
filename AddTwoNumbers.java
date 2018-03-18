/**
 * Question:
 * You are given two linked lists representing two non-negative numbers. 
 * The digits are stored in reverse order and each of their nodes contain 
 * a single digit. Add the two numbers and return it as a linked list.
 * 
 * Example:
 * Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
 * Output: 7 -> 0 -> 8
 * 
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class AddTwoNumbers {
	public ListNode addTwoNumbers(ListNode l1, ListNode l2){
		ListNode l1c = l1;
		ListNode l2c = l2;
		int fistVal = (l1c.val + l2c.val)%10;
		int c = (l1c.val + l2c.val) >= 10? 1:0;
		ListNode ans = new ListNode(fistVal);
		ListNode ansEnd = ans;

		l1c = l1c.next;
		l2c = l2c.next;
		
		while(l1c != null && l2c != null){
			ansEnd = addNode((l1c.val + l2c.val + c)%10,ansEnd);
			c = (l1c.val + l2c.val +c ) >= 10? 1:0;
			l1c = l1c.next;
			l2c = l2c.next;
		}
		if(l1c == null){
			while(l2c != null){
				ansEnd = addNode((l2c.val + c)%10,ansEnd);
				c = (l2c.val + c) >= 10? 1:0;
				l2c = l2c.next;
			}
		}
		if(l2c == null){
			while(l1c != null){
				ansEnd = addNode((l1c.val + c)%10,ansEnd);
				c = (l1c.val + c) >= 10? 1:0;
				l1c = l1c.next;
			}
		}
		if(c == 1){
			ansEnd = addNode(1,ansEnd);
		}
		return ans;
	}
	
	public static ListNode addNode(int val, ListNode end){
		ListNode tmp = new ListNode(val);
		end.next = tmp;
		return tmp;
	}
}	
/*
 * a more succinct version from leetcode
 */
//	ListNode dummyHead = new ListNode(0);
//    ListNode p = l1, q = l2, curr = dummyHead;
//    int carry = 0;
//    while (p != null || q != null) {
//        int x = (p != null) ? p.val : 0;
//        int y = (q != null) ? q.val : 0;
//        int sum = carry + x + y;
//        carry = sum / 10;
//        curr.next = new ListNode(sum % 10);
//        curr = curr.next;
//        if (p != null) p = p.next;
//        if (q != null) q = q.next;
//    }
//    if (carry > 0) {
//        curr.next = new ListNode(carry);
//    }
//    return dummyHead.next;
	
/*
 * another method 
 * transform the two linklists into two number
 * calculate their sum then transform the sum into a linklist
 * not work for big int	
 */
//	long l1Int = l1.val;
//	long l2Int = l2.val;
//	long ansInt = 0;
//	ListNode ans = new ListNode(0);
//	ListNode ansEnd = ans;
//	
//	int pow = 1;
//	while(l1.next != null){
//		l1 = l1.next;
//		l1Int += l1.val*Math.pow(10, pow++);
//	}
//	System.out.println(l1Int);
//	pow = 1;
//	while(l2.next != null){
//		l2 = l2.next;
//		l2Int += l2.val*Math.pow(10, pow++);
//	}
//	System.out.println(l2Int);
//	ansInt = l1Int + l2Int;
//	System.out.println(ansInt);
//	while(ansInt/10 > 0){
//		ansEnd = addNode((int)(ansInt%10), ansEnd);
//		ansInt /= 10;
//	}
//	ansEnd = addNode((int)ansInt, ansEnd);
//	return ans.next;	//abandon the first node which is 0
//}
