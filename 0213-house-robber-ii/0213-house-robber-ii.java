class Solution {
    public int rob(int[] nums) {
        if(nums.length<=3) return findMax(nums);
        int[] dp1 = new int[nums.length-1];
        int[] dp2 = new int[nums.length-1];

        dp1[0] = nums[0];
        dp2[0] = nums[1];

        dp1[1] = Math.max(nums[0],nums[1]);
        dp2[1] = Math.max(nums[1],nums[2]);

        for(int i=2;i<nums.length-1;i++){
            dp1[i] = Math.max(dp1[i-2]+nums[i],dp1[i-1]);
            dp2[i] = Math.max(dp2[i-2]+nums[i+1],dp2[i-1]);
        }
        return Math.max(dp1[dp1.length-1],dp2[dp2.length-1]);
    }

    public int findMax(int[] nums){
        int maximum = nums[0];
        for(int i=1; i<nums.length; i++) maximum = Math.max(maximum,nums[i]);
        return maximum;
    }
}