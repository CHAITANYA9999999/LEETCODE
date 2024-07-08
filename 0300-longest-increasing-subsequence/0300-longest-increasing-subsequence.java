class Solution {
    public int lengthOfLIS(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n];
        Arrays.fill(dp,1);
        for(int i=n-2; i>=0; i--) for(int j=i+1; j<n; j++) if(nums[i]<nums[j]) dp[i] = Math.max(dp[i],1+dp[j]);
        return getMax(dp);
    }

    public static int getMax(int[] a){ 
		int max = 0; 
		for (int i = 0; i<a.length; i++) { 
			if(a[i] > max) max = a[i]; 
		} 
		return max; 
	} 
}