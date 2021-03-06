"""
155. Min Stack
Easy

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 

Constraints:

-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.
"""

#Success
# Details 
# Runtime: 51 ms, faster than 81.28% of Python online submissions for Min Stack.
# Memory Usage: 17.1 MB, less than 67.75% of Python online submissions for Min Stack.

class MinStack(object):

    def __init__(self):
        self.minStack = []
        self.minimum = float('inf')

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.minStack.append(val)
        if self.minimum > val:
            self.minimum = val
        
    def pop(self):
        """
        :rtype: None
        """
        popped = self.minStack.pop()
        if popped == self.minimum:
            temp = float('inf')
            for num in self.minStack:
                if num < temp:
                    temp = num
            self.minimum = temp
        return popped

    def top(self):
        """
        :rtype: int
        """
        return self.minStack[len(self.minStack) -1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minimum



# Your MinStack object will be instantiated and called as such:
val = -2
val2 = 0
val3 = -3
obj = MinStack()
obj.push(val)
obj.push(val2)
obj.push(val3)
param_4 = obj.getMin() #return -3
obj.pop()
param_3 = obj.top() # 
#param_4 = obj.getMin()
print(param_3)
print(param_4)