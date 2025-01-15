class Solution {
    public boolean isPalindrome(int x) {
        // If the number is negative, it's not a palindrome
        if (x < 0) {
            return false;
        }

        int n = x; // Copy the original number
        int revNum = 0; // This will store the reversed number

        // Reverse the number
        while (n > 0) {
            int d = n % 10; // Extract the last digit
            revNum = revNum * 10 + d; // Add the digit to revNum
            n = n / 10; // Remove the last digit from n
        }

        // Compare the reversed number with the original
        return revNum == x; // Return true if they are the same, false otherwise
    }
}

/*
Example: x = 121

Step 1: Initial Setup
    n = 121, revNum = 0

Step 2: First Iteration of the While Loop
    d = n % 10 = 121 % 10 = 1 (last digit)
    revNum = revNum * 10 + d = 0 * 10 + 1 = 1
    n = n / 10 = 121 / 10 = 12

Step 3: Second Iteration of the While Loop
    d = n % 10 = 12 % 10 = 2 (last digit)
    revNum = revNum * 10 + d = 1 * 10 + 2 = 12
    n = n / 10 = 12 / 10 = 1

Step 4: Third Iteration of the While Loop
    d = n % 10 = 1 % 10 = 1 (last digit)
    revNum = revNum * 10 + d = 12 * 10 + 1 = 121
    n = n / 10 = 1 / 10 = 0 (end loop)

Step 5: Compare
    revNum (121) == x (121)
    Result: true (It's a palindrome)

---

Time Complexity Analysis:
1. **Reversing the number:** 
   - The `while` loop runs once for each digit in the number.
   - If the number has `d` digits, the loop runs `d` times.
   - Each iteration involves constant-time operations (`%`, `*`, `+`, `/`), so the time complexity is **O(d)**.

2. **Digits in a number (`d`):**
   - The number of digits in a number `x` is approximately `log10(x)`.
   - Therefore, the overall time complexity is **O(log10(x))**.

Space Complexity:
- The algorithm uses a constant amount of space for variables (`n`, `revNum`, `d`).
- Hence, the space complexity is **O(1)**.
*/
