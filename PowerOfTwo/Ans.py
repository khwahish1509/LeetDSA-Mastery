class Solution {
    public boolean isPowerOfTwo(int n) {
        // If the number is less than 1, it's not a power of two
        if (n < 1) {
            return false;
        } 
        // 1 is a power of two (2^0 = 1)
        else if (n == 1) {
            return true;
        } 
        // Check divisibility by 2
        else {
            while (n % 2 == 0) { // If divisible by 2
                n = n / 2;       // Keep dividing n by 2
            }

            // If after dividing, n becomes 1, it's a power of two
            if (n == 1) {
                return true;
            } else {
                return false;
            }
        }
    }
}

/*
Example: n = 16

Step 1: Initial Setup
    n = 16

Step 2: Check divisibility and divide by 2 repeatedly
    - First iteration: n % 2 == 0 → n = n / 2 = 16 / 2 = 8
    - Second iteration: n % 2 == 0 → n = n / 2 = 8 / 2 = 4
    - Third iteration: n % 2 == 0 → n = n / 2 = 4 / 2 = 2
    - Fourth iteration: n % 2 == 0 → n = n / 2 = 2 / 2 = 1

Step 3: Final Check
    After dividing, n == 1 → Return true (16 is a power of two).

---

Time Complexity Analysis:
1. **Dividing by 2:**
   - The loop runs as long as `n % 2 == 0`.
   - In each iteration, `n` is divided by 2, reducing `n` to half.
   - This process continues approximately `log2(n)` times (since dividing by 2 repeatedly reduces `n` exponentially).

   **Time Complexity: O(log2(n))**

2. **Space Complexity:**
   - The algorithm uses a constant amount of space for variables (`n`).
   - **Space Complexity: O(1)**

*/
