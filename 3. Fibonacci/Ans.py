class Solution {
    public int fib(int n) {
        // Base cases
        if (n == 0) {
            return 0;
        } else if (n == 1) {
            return 1;
        }

        int firstTerm = 0;
        int secondTerm = 1;

        // Iterate to calculate the Fibonacci number
        for (int i = 2; i <= n; i++) {
            int thirdTerm = firstTerm + secondTerm;
            firstTerm = secondTerm;
            secondTerm = thirdTerm;
        }

        return secondTerm; // Return the nth Fibonacci number
    }
}

/*
Example: n = 5

Step 1: Initial Setup
    n = 5

Step 2: Calculate Fibonacci numbers iteratively
    - First iteration: firstTerm = 0, secondTerm = 1 → thirdTerm = 0 + 1 = 1
    - Second iteration: firstTerm = 1, secondTerm = 1 → thirdTerm = 1 + 1 = 2
    - Third iteration: firstTerm = 1, secondTerm = 2 → thirdTerm = 1 + 2 = 3
    - Fourth iteration: firstTerm = 2, secondTerm = 3 → thirdTerm = 2 + 3 = 5

Step 3: Final Check
    After iterating, the Fibonacci number is 5 → Return 5 (5 is the 5th Fibonacci number).

---

Time Complexity Analysis:
1. **Iterating through the loop:**
   - The loop runs from 2 to `n` (inclusive).
   - The operations inside the loop (addition and assignment) are constant time operations.
   - This means the time complexity is proportional to `n`.

   **Time Complexity: O(n)**

2. **Space Complexity:**
   - The algorithm uses a constant amount of space for variables (`firstTerm`, `secondTerm`, and `thirdTerm`).
   - **Space Complexity: O(1)**
*/
