class Solution {
    public int numWaterBottles(int numBottles, int numExchange) {
        // Start with the given number of bottles
        int ans = numBottles;

        // Keep exchanging bottles until you can't exchange anymore
        while (numBottles >= numExchange) {
            int newBottles = numBottles / numExchange; // Bottles obtained from exchange
            int remBottles = numBottles % numExchange; // Leftover bottles

            ans = ans + newBottles; // Add new bottles to the total count
            numBottles = newBottles + remBottles; // Update the total bottles available
        }

        return ans; // Return the total number of bottles drunk
    }
}

/*
Example: numBottles = 9, numExchange = 3

Step 1: Initial Setup
    ans = 9 (start with 9 bottles)

Step 2: First Exchange
    newBottles = 9 / 3 = 3 (3 new bottles from exchange)
    remBottles = 9 % 3 = 0 (no leftover bottles)
    ans = ans + newBottles = 9 + 3 = 12 (total bottles drunk so far)
    numBottles = newBottles + remBottles = 3 + 0 = 3 (bottles available for next round)

Step 3: Second Exchange
    newBottles = 3 / 3 = 1 (1 new bottle from exchange)
    remBottles = 3 % 3 = 0 (no leftover bottles)
    ans = ans + newBottles = 12 + 1 = 13 (total bottles drunk so far)
    numBottles = newBottles + remBottles = 1 + 0 = 1 (bottles available for next round)

Step 4: End Condition
    numBottles < numExchange → Stop exchanging
    Return ans = 13

---

Time Complexity Analysis:
1. **Loop Execution:**
   - The number of iterations depends on how many times we can exchange bottles.
   - At each step, the number of bottles decreases by a factor of `numExchange`.
   - This is approximately logarithmic in terms of the initial `numBottles`.
   - **Time Complexity: O(log(numBottles))**

2. **Space Complexity:**
   - The algorithm uses a constant amount of space for variables (`ans`, `newBottles`, `remBottles`).
   - **Space Complexity: O(1)**

*/
