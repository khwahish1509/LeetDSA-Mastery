class Solution {
    public List<Integer> addToArrayForm(int[] num, int k) {
        // Result array to store digits
        List<Integer> ans = new ArrayList<>();

        // Pointer for the last index of the array
        int p = num.length - 1;

        // Carry value
        int carry = 0;

        // Loop while there are digits left in the array or in k, or there's a carry
        while (p >= 0 || k > 0) {
            int numval = 0;

            // If the pointer is valid, get the digit from the array
            if (p >= 0) {
                numval = num[p];
            }

            int d = k % 10; // Extract the last digit of k

            // Calculate the sum of the current digit, the last digit of k, and carry
            int sum = numval + d + carry;

            // Extract the last digit of the sum and update the carry
            int digit = sum % 10;
            carry = sum / 10;

            // Add the digit to the result
            ans.add(digit);

            // Remove the last digit from k
            k = k / 10;

            // Move the pointer for the array
            p--;
        }

        // If there is still a carry left, add it to the result
        if (carry > 0) {
            ans.add(carry);
        }

        // Reverse the result as digits were added in reverse order
        Collections.reverse(ans);

        return ans; // Return the final list of digits
    }
}

/*
Example:
Input: num = [2, 7, 4], k = 181

Step-by-Step Execution:
1. Initial Setup:
   p = 2 (pointing to the last digit of the array)
   carry = 0
   k = 181

2. Iteration 1:
   numval = num[2] = 4
   d = k % 10 = 1
   sum = numval + d + carry = 4 + 1 + 0 = 5
   digit = sum % 10 = 5
   carry = sum / 10 = 0
   ans = [5]
   k = k / 10 = 18
   p = 1

3. Iteration 2:
   numval = num[1] = 7
   d = k % 10 = 8
   sum = numval + d + carry = 7 + 8 + 0 = 15
   digit = sum % 10 = 5
   carry = sum / 10 = 1
   ans = [5, 5]
   k = k / 10 = 1
   p = 0

4. Iteration 3:
   numval = num[0] = 2
   d = k % 10 = 1
   sum = numval + d + carry = 2 + 1 + 1 = 4
   digit = sum % 10 = 4
   carry = sum / 10 = 0
   ans = [5, 5, 4]
   k = k / 10 = 0
   p = -1

5. Final Step:
   No carry left, reverse the result:
   ans = [4, 5, 5]

Output:
[4, 5, 5]

---

Time Complexity Analysis:
1. **Iteration:**
   - The loop runs for a maximum of `max(num.length, log₁₀(k))` iterations.
   - **Time Complexity: O(max(n, log(k)))**, where `n` is the size of the array `num`.

2. **Reversal:**
   - Reversing the list takes **O(n)** time.
   - Final time complexity: **O(max(n, log(k)))**

3. **Space Complexity:**
   - The result list `ans` grows with the size of the result, which can be at most `n + 1`.
   - **Space Complexity: O(n)**

*/
