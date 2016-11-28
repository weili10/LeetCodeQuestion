/*
 * Question:
 * There are two sorted arrays nums1 and nums2 of size m and n respectively.
 * Find the median of the two sorted arrays. The overall run time complexity 
 * should be O(log (m+n)).
 * 
 * Example:
 * nums1 = [1, 3]
 * nums2 = [2]
 * The median is 2.0
 * 
 * nums1 = [1, 2]
 * nums2 = [3, 4]
 * The median is (2 + 3)/2 = 2.5
 */
public class FindMedianSortedArrays {
	public double findMedianSortedArrays(int[] nums1, int[] nums2) {
		int total = nums1.length + nums2.length;
		if(total%2 == 0){
			return (findKth(nums1, 0, nums2, 0, total/2)+findKth(nums1, 0, nums2, 0, total/2+1))/2;
		}
		else{
			return findKth(nums1, 0, nums2, 0, total/2+1);
		}
		
	}
	
	public double findKth(int[] nums1, int st1, int[] nums2,int st2, int k){
		int n1 = nums1.length - st1;
		int n2 = nums2.length - st2;
		if(n1 > n2){
			return findKth(nums2,st2,nums1,st1,k);   //make n1 <= n2
		}
		if(n1 == 0){
			return nums2[k-1];
		}
		if(k == 1){
			return Math.min(nums1[st1], nums2[st2]);
		}
		
		int p1 = Math.min(n1, k/2);
		int p2 = k - p1;
		if(nums1[st1+p1-1] < nums2[st2+p2-1]){
			return findKth(nums1, st1+p1, nums2, st2, k-p1);
		}else if(nums1[st1+p1-1] > nums2[st2+p2-1]){
			return findKth(nums1, st1, nums2, st2+p2, k-p2);
		}else{
			return nums1[st1+p1-1];
		}
	}
}
