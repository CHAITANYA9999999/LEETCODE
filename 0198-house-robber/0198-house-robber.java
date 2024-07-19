class Solution {
    public int rob(int[] nums) {
        int[] memo = new int[nums.length + 1];
        memo[0]=0;
        memo[1]=nums[0];
        for(int i=1;i<nums.length;i++){
            int val = nums[i];
            memo[i+1] = Math.max(val+memo[i-1],memo[i]);
        }
        return memo[nums.length];
    }
}