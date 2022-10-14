 Solution - I (Brute-Force)

Let's try solving with brute-force approach. For each house, we have two choices -

Dont rob the house and move to next house.
Rob the house and move to the house after next house (We dont move directly to next house because we can rob adjacent houses).
So, we will just try with both these choices and choose the one the yields the maximum amount of loot.



class Solution:
    def rob(self, A, i = 0):
        return max(self.rob(A, i+1), A[i] + self.rob(A, i+2)) if i < len(A) else 0
      
      
Time Complexity : O(2N), where N is the number of elements in A. At each index, we have two choices of either robbing or not robbing the current house. Thus this leads to time complexity of 2*2*2...n times ≈ O(2N)
Space Complexity : O(N), required by implicit recursive stack. The max depth of recursion can go upto N.
  
Solution - II (Dynamic Programming - Memoization)

In the above solution, we were performing many redundant repeated computations. This can be observed by drawing out the recursive tree for above function and observing that rob(i) is called multiple times. But rob(i) is nothing but the maximum amount of loot we can get starting at index i and this amount remains the same at each call.

So, instead of re-computing multiple times, we can store the result of a function call and directly reuse it on future calls instead of recomputing from scratch. This calls for dynamic programming, or memoization to be more specific. Here, we can use a linear dp array where dp[i] will denote the maximum amount of loot we can get starting at i index. Initially all elements of dp are initialized to -1 denoting they haven't been computed yet, Each time, we will save the computed result in this dp for an index i and directly return it if a future call is made to this index.



class Solution:
    def rob(self, A):
        @cache
        def rob(i):
            return max(rob(i+1), A[i] + rob(i+2)) if i < len(A) else 0
        return rob(0)
      
      
Time Complexity : O(N), We calculate the result for each index only once & there are N indices. Thus overall time complexity is O(N).
Space Complexity : O(N), required for dp and implicit recursive stack.


  
