# Algorithm

This dictionary help me to organize my algorithm problems. Read this document help me quickly review the core content of various algorithms.

## Core Techniques Summary

### Two Pointers

- Same direction: sliding window
- Opposite direction: sorted array problems

### Sliding Window

- Fixed size window
- Variable size window

### Fast and Slow Pointers

- Cycle detection
- Find middle element

### DFS vs BFS

- DFS: path finding, backtracking
- BFS: shortest path, level traversal

### Divide and Conquer

- Binary search
- Merge sort
- Quick sort

## Array

### Two Pointers (双指针)

- **Valid Subsequence** (Easy) - [`isValidSubsequence`](arrays-eazy/isValidSubsequence.py)
- **Sweet and Savory** (Medium) - [`sweetAndSavory`](arrays-medium/sweetAndSavory.py)

### Prefix Sum (前缀和)

- **Subarray Sum** (Medium) - [`subarraySum`](arrays-medium/subarraySum.py)

### Product Array (乘积数组)

- **Array of Products** (Medium) - [`arrayOfProducts`](arrays-medium/arrayOfProducts.py)

### Greedy (贪心算法)

- **Non-Constructible Change** (Easy) - [`nonConstructibleChange`](arrays-eazy/nonConstructibleChange.py)

### Mathematical Approach (数学方法)

- **Missing Numbers** (Medium) - [`missingNumbers`](arrays-medium/missingNumbers.py)

## HashMap

### Frequency Counting (频次统计)

- **Generate Document** (Easy) - [`generateDocument`](string-eazy/generateDocument.py)

### Prefix Sum + HashMap

- **Subarray Sum** (Medium) - [`subarraySum`](arrays-medium/subarraySum.py)

### Sliding Window + HashMap

- **Longest Substring** (Medium) - [`lengthOfLongestSubstring`](string-medium/lengthOfLongestSubstring.py)
- **Find Anagrams** (Medium) - [`findAnagrams`](string-medium/findAnagrams.py)

## String

### Two Pointers (双指针)

- **One Edit** (Medium) - [`oneEdit`](string-medium/oneEdit.py)

### Sliding Window (滑动窗口)

- **Longest Substring** (Medium) - [`lengthOfLongestSubstring`](string-medium/lengthOfLongestSubstring.py)
- **Find Anagrams** (Medium) - [`findAnagrams`](string-medium/findAnagrams.py)

### Character Frequency (字符频次)

- **Generate Document** (Easy) - [`generateDocument`](string-eazy/generateDocument.py)

## Stack

### Monotonic Stack (单调栈)

- **Next Greater Element** (Medium) - [`nextGreaterElement`](stacks/nextGreaterElement.py)

### Expression Evaluation (表达式求值)

- Parentheses matching
- Infix to postfix conversion

## Queue

### BFS (广度优先搜索)

- **Breadth First Search** (Easy) - [`breadthFirstSearch`](graphs/breadthFirstSearch.py)
- **Minimum Passes of Matrix** (Medium) - [`minimumPassesOfMatrix`](graphs/minimumPassesOfMatrix.py)

### Level Order Traversal (层序遍历)

- Binary tree level traversal

## Linked List

### Fast and Slow Pointers (快慢指针)

- **Find the middle one** - 快慢指针找中点
- **Detect Cycle** (Medium) - [`detectCycle`](linked-list/detectCycle.py)

### Reverse (反转)

- **Reverse Linked List** - [`reverse_linked_list`](linked-list/basic-op.py)
- **Inverted Bisection** (Medium) - [`invertedBisection`](algo-assessments/invertedBisection.py)

### Arithmetic Operations (算术运算)

- **Sum of Linked Lists** (Medium) - [`sumOfLinkedLists`](linked-list/sumOfLinkedLists.py)

### Node Manipulation (节点操作)

- **Remove Node** - 删除节点
- **DeepCopy** - 深度复制

## Binary Tree

### BFS Traversal (广度优先遍历)

- **Level Order Traversal** (Medium) - [`levelOrder`](binary-tree/levelOrder.py)
- **Zigzag Level Order Traversal** (Medium) - [`zigzagLevelOrder`](binary-tree/zigzagLevelOrder.py)

### DFS Traversal (深度优先遍历)

- **Branch Sums** (Easy) - [`branchSums`](binary-tree/branchSums.py)
- **Symmetric Tree** (Easy) - [`symmetricTree`](binary-tree/symmetricalTree.py)
- **Lowest Common Ancestor** (Medium) - [`lowestCommonAncestor`](binary-tree/lowestCommonAncestor.py)
- **Build Tree** (Medium) - [`buildTree`](binary-tree/buildTree.py)

### Tree Properties (树的性质)

- **Height Balanced** (Medium) - [`heightBalancedBinaryTree`](binary-tree/heightBalancedBinaryTree.py)

### Tree Manipulation (树的操作)

- **Split Binary Tree** (Medium) - [`splitBinaryTree`](binary-tree/splitBinaryTree.py)
- **Merge Binary Trees** (Easy) - [`mergeBinaryTrees`](binary-tree/mergeBinaryTrees.py)

## Binary Search Tree

### BST Validation (BST 验证)

- **Validate BST** (Medium) - [`validateBst`](binary-search-tree/validateBst.py)

### BST Traversal using DFS (BST 遍历)

- **In-order, Pre-order, Post-order** (Easy) - [`traversal`](binary-search-tree/traversal.py)

## Searching

### Binary Search (二分查找)

- **Binary Search** (Easy) - [`binarySearch`](searching/binarySearch.py)

### Divide and Conquer (分治法)

- Binary search variations
- Find peak element

## Sorting

### Selection Sort (选择排序)

- **Selection Sort** (Easy) - [`selectionSort`](sort-eazy/selectionSort.py)

### Heap Sort (堆排序)

- **Heap Sort** (Medium) - [`heapSort`](sort-medium/heapSort.py)

### Three-way Partitioning (三路快排)

- **Three Number Sort** (Medium) - [`threeNumberSort`](sort-medium/threeNumberSort.py)

## Heaps

### Heap Operations (堆操作)

- **Min Heap** (Medium) - [`MinHeap`](heaps/minHeap.py)
  - `buildHeap`, `siftUp`, `siftDown`
  - `insert`, `remove`, `peek`

### Priority Queue (优先队列)

- Task scheduling
- Top K problems

## Graphs

### DFS (深度优先搜索)

- **Depth First Search** (Easy) - [`depthFirstSearch`](graphs/depthFirstSearch.py)
- **Remove Islands** (Medium) - [`removeIslands`](graphs/removeIslands.py)

### BFS (广度优先搜索)

- **Breadth First Search** (Easy) - [`breadthFirstSearch`](graphs/breadthFirstSearch.py)
- **Minimum Passes of Matrix** (Medium) - [`minimumPassesOfMatrix`](graphs/minimumPassesOfMatrix.py)

### Cycle Detection (环检测)

- **Cycle in Graph** (Medium) - [`cycleInGraph`](graphs/cycleInGraph.py)

### Connected Components (连通分量)

- **Remove Islands** (Medium) - [`removeIslands`](graphs/removeIslands.py)

## Recursion

### Memoization (记忆化)

- **Nth Fibonacci** (Easy) - [`getNthFib`](recursion-eazy/getNthFib.py)

### Backtracking (回溯)

- Permutations and combinations
- Path finding

## Dynamic Programming

### Coin Change (硬币找零)

- **Min Coins for Change** (Medium) - [`minNumberOfCoinsForChange`](dp-medium/minNumberOfCoinsForChange.py)

### Optimal Substructure (最优子结构)

- State transition equations
- Bottom-up approach

## Greedy Algorithms

### Task Scheduling (任务调度)

- **Task Assignment** (Medium) - [`taskAssignment`](greedy-algorithms/taskAssignment.py)

### Maximum Subarray (最大子数组)

- **Kadane's Algorithm** (Medium) - [`kadanesAlgorithm`](famous-algorithms/kadanesAlgorithm.py)

## Pattern Matching

### Dynamic Programming Matching

- **Glob Matching** (Hard) - [`globMatching`](algo-assessments/globMatching.py)

### Wildcard Patterns

- `*` and `?` matching
- Regular expressions
