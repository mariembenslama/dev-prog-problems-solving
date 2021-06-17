# dev-prog-problems-solving


Search Tree:
  - is Binary search tree algorithm (written in python)
  - Time complexity => O(log(n)) [as it divides search in sub trees - root and it's 2 children]
  - Space complexity => O(n) [as n is number of nodes]
  - The search algorithm depends on the height of the tree, unless in worst case it's only one branch of the tree, it makes 
  the complexity of the algorithm O(n)

| Height  | Nodes | Log calculation |
| ------------- | ------------- | ------------- |
| 0  | 1  | log2(1) = 0  |
| 1  | 3 | log2(3) = 1 |
| 2  | 7  | log2(7) = 2  |
| 3  | 15 | log2(15) = 3   |

Reverse Linked List:
   - Linked list: [{value, next} ...]
   - Reversing [1,2,3] => [3,2,1]
   - Algorithm used: => head.next.next: if head is [1] then next.next => [2,1] and head.next = none
   - The time and space complexity of the algorithm is O(n) since we should pass through the whole linked list and its elements + it stores all the nodes of the list.
   
Max Element Stack:
   - 2 arrays: stack, maxes
   - Stack has all elements, maxes has only max value per push
   - Last element of maxes contains the max element of the stack
   - Time and space complexity are both O(n): since we check all the stack and we store all elements, since having 2 arrays means double instruction O(2n) -> O(const * n) -> O(n)

Adjacent List (Graph):
   - Preparing a graph and determine a cycle inside
   - List of prerequisities that can contain a loop (1 -> 0, 0 -> 1: loop), (1 -> 0, 1 -> 2: not loop)
   - Algorithm: 
      1. Draw the graph
      2. Visit vertexes and their neighboors -> store the neighboors temporarily in a visited set
      3. Check if each neighboor is already visited (using recursion)
      4. Return True if the neighboor is already visited -> means there's cycle
      5. Print can Finish: False if 4. Has happened
      6. If 4. didn't happen, return false if each node in the graph and their neighboor hasn't been visited and there's no cycle
      7. Print can Finish: True  if 6. Has happened
   - Space Complexity is O(n) since we need to store all nodes
   - Time complexity is O(n^2) since program should visit all nodes and all of their connected neighboors
