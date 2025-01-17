class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Create an array to store the result
        int[] ans = new int[2];

        // Loop through each pair of numbers in the array
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                // Check if the sum of nums[i] and nums[j] equals the target
                if (nums[i] + nums[j] == target) {
                    ans[0] = i; // Store the first index
                    ans[1] = j; // Store the second index
                    return ans; // Return the answer immediately
                }
            }
        }

        return ans; // In case no solution is found (though the problem guarantees one)
    }
}

/* 
Example:
nums = [2, 7, 11, 15]
target = 9

Step-by-Step Execution:
1. Outer loop starts with i = 0:
    - Inner loop starts with j = 1:
        nums[0] + nums[1] = 2 + 7 = 9 (equals target)
        → Store indices in `ans`: ans[0] = 0, ans[1] = 1
        → Return [0, 1]

Output:
[0, 1]

---

Time Complexity Analysis:
1. **Nested Loops:**
   - The outer loop runs `n` times, where `n` is the size of the `nums` array.
   - The inner loop runs approximately `n - 1` times on the first iteration, `n - 2` on the second, and so on.
   - Total iterations: `n + (n-1) + (n-2) + ... + 1 = n(n-1)/2`.
   - **Time Complexity: O(n²)**

2. **Space Complexity:**
   - The algorithm uses constant space for the `ans` array (size 2).
   - **Space Complexity: O(1)**
*/
