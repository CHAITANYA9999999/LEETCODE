import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        int n = nums.length;

        for (int i = 0; i < n - 3; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;  // Skip duplicates for i
            for (int j = i + 1; j < n - 2; j++) {
                if (j > i + 1 && nums[j] == nums[j - 1]) continue;  // Skip duplicates for j
                int l = j + 1, r = n - 1;
                long remaining = (long)target - nums[i] - nums[j]; // Use long to avoid overflow
                while (l < r) {
                    long sum = (long)nums[l] + nums[r];
                    if (sum == remaining) {
                        res.add(new ArrayList<>(Arrays.asList(nums[i], nums[j], nums[l], nums[r])));
                        while (l < r && nums[l] == nums[l + 1]) l++;  // Skip duplicates for l
                        while (l < r && nums[r] == nums[r - 1]) r--;  // Skip duplicates for r
                        l++;
                        r--;
                    } else if (sum < remaining) {
                        l++;
                    } else {
                        r--;
                    }
                }
            }
        }
        return res;
    }
}
